import requests
from bs4 import BeautifulSoup
import csv
import time
import re

# Base URL pointing to the Wayback Machine archive for the clinic directory
BASE_ARCHIVE_URL = "https://web.archive.org/web/20250708180027"
MAIN_CLINIC_PATH = "/https://www.myfootdr.com.au/our-clinics/"
START_URL = BASE_ARCHIVE_URL + MAIN_CLINIC_PATH

def get_full_url(path):
    """
    Constructs the full Wayback Machine URL from a partial or relative path.
    """
    # Fix broken paths often found in archived sites
    if path and path.startswith("//"):
        path = "https:" + path

    # If the path is already a full archive URL, return it
    if path and path.startswith(BASE_ARCHIVE_URL):
        return path
        
    # Assume the path is a relative link and prepend the archive base
    if path and path.startswith("/"):
        return BASE_ARCHIVE_URL + path.replace(BASE_ARCHIVE_URL, "") # Ensure we don't duplicate the prefix
    
    return path


def get_soup(url, max_retries=3):
    """Fetches and parses HTML with basic retries and headers for robustness."""
    # print(f"-> Fetching: {url}")
    for attempt in range(max_retries):
        try:
            # Be polite to the server, especially on the Wayback Machine
            time.sleep(1) 
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            return BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            # print(f"Error fetching {url} (Attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt) # Exponential backoff
            else:
                return None
    return None

def scrape_clinic_page(clinic_url):
    """Scrapes the Name, Address, Email, Phone, and Services from a single clinic page."""
    data = {
        'Name of Clinic': '', 
        'Address': '', 
        'Email': '', 
        'Phone': '', 
        'Services': ''
    }
    soup = get_soup(clinic_url)
    if not soup:
        return data

    # 1. Name of Clinic: Find the main heading
    h1_tag = soup.find('h1')
    data['Name of Clinic'] = h1_tag.text.strip() if h1_tag else ''

    # 2. Email: Find link with 'mailto:'
    email_tag = soup.find('a', href=lambda href: href and href.startswith("mailto:"))
    data['Email'] = email_tag['href'].replace('mailto:', '').strip() if email_tag else ''

    # 3. Phone: Find link with 'tel:'
    phone_tag = soup.find('a', href=lambda href: href and href.startswith("tel:"))
    # Use the link text, then clean up extraneous characters often used for icons
    if phone_tag:
        phone_text = phone_tag.get_text(strip=True)
        # Remove non-numeric characters except spaces and common grouping characters
        data['Phone'] = re.sub(r'[^0-9\s\(\)\+]+', '', phone_text).strip()
    
    # 4. Address: This is the trickiest. Look for the contact info block.
    # Often contained in a link that gives directions or is near the email/phone.
    address_element = soup.find('a', href=lambda href: href and 'google.com/maps' in href)
    
    if address_element and address_element.previous_sibling:
        # The address text is often found just before the map link or as the text of an icon-link.
        # Check the direct sibling for the address line if the map link text is just 'Get directions'
        address_node = address_element.previous_sibling
        # Look for the element that holds the full address text (often an <i> tag sibling)
        address_container = soup.find('i', class_=lambda c: c and ('map-marker' in c or 'address' in c))
        if address_container and address_container.next_sibling and address_container.next_sibling.name == 'a':
             # The address is the text content of the link next to the icon
             data['Address'] = address_container.next_sibling.get_text(separator=', ', strip=True)
        elif address_node and address_node.text.strip():
            # Fallback: check previous text node
            data['Address'] = address_node.text.strip().replace('\n', ', ')
            
    # Clean up common address remnants
    data['Address'] = re.sub(r', ,', ', ', data['Address']).strip()

    # 5. Services: Look for the clear list of services (e.g., unordered list `<ul>`)
    services_list = []
    # Find the paragraph or header that introduces the services list (e.g., 'will be able to assist with:')
    services_intro = soup.find(lambda tag: tag.name in ['p', 'h2', 'h3'] and ('assist with' in tag.get_text() or 'services' in tag.get_text().lower()))
    
    if services_intro:
        # Find the next immediate unordered list
        ul_tag = services_intro.find_next('ul')
        if ul_tag:
            services_list = [li.text.strip() for li in ul_tag.find_all('li') if li.text.strip()]
            data['Services'] = ", ".join(services_list)
    
    # Simple cleanup to remove excess whitespace
    data['Services'] = re.sub(r'\s{2,}', ' ', data['Services']).strip()

    return data

def scrape_all_clinics():
    """Main function to orchestrate the scraping process."""
    print("Starting clinic data scrape from My FootDr archive...")
    
    soup = get_soup(START_URL)
    if not soup:
        print("Failed to fetch main clinic page. Check URL and connectivity.")
        return

    clinic_data_list = []
    processed_clinic_paths = set()

    # 1. Find Region Links: Target the navigation menu links to regions
    # Links are usually in the format /our-clinics/regions/statename/
    region_tags = soup.select('nav a[href*="/our-clinics/regions/"]')
    
    # 2. Iterate through regions to find individual clinic links
    for region_tag in region_tags:
        region_url = get_full_url(region_tag['href']).split('#')[0] # Remove potential #jump links
        
        region_soup = get_soup(region_url)
        if not region_soup:
            continue
            
        region_name = region_tag.text.strip()
        
        # Select individual clinic links on the region page.
        # Clinic links are typically inside <h4> or directly in the content block
        clinic_tags = region_soup.select('h4 a[href*="/our-clinics/"]')
        
        if not clinic_tags:
            # Fallback selector for clinics listed without H4 (e.g., div with class .clinic-block)
             clinic_tags = region_soup.select('div a[href*="/our-clinics/"]:not([href*="/regions/"]):not([href*="#"])')

        clinic_urls = [get_full_url(a['href']) for a in clinic_tags]
        
        print(f"--- Processing Region: {region_name} ({len(clinic_urls)} potential clinics) ---")

        # 3. Scrape each unique clinic page
        for clinic_url in clinic_urls:
            # Extract the unique part of the path (e.g., 'noosa', 'brisbane-cbd') to check uniqueness
            clean_path = re.search(r'/our-clinics/([^/]+)/?$', clinic_url)
            if not clean_path:
                continue
                
            unique_path_id = clean_path.group(1)
            
            # Prevent redundant scraping
            if unique_path_id in processed_clinic_paths:
                continue
            
            processed_clinic_paths.add(unique_path_id)
            
            # Scrape the data
            clinic_data = scrape_clinic_page(clinic_url)
            
            if clinic_data.get('Name of Clinic'):
                clinic_data_list.append(clinic_data)
                # print(f"  > Scraped: {clinic_data['Name of Clinic']}")

    # 4. Save to CSV
    keys = ['Name of Clinic', 'Address', 'Email', 'Phone', 'Services']
    filename = 'clinics_data.csv'
    
    print(f"\n--- Scraping complete. Total unique clinics scraped: {len(clinic_data_list)} ---")
    
    if clinic_data_list:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(clinic_data_list)
        print(f"Data successfully saved to {filename}.")
    else:
        print("No clinic data was successfully scraped to save.")

if __name__ == "__main__":
    # Note: Running this script requires the necessary Python libraries (requests, beautifulsoup4) 
    # and stable internet access to the Wayback Machine archive.
    scrape_all_clinics()