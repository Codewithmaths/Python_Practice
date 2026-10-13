from bs4 import BeautifulSoup
import requests


html_doc = """
<html>
<head>
  <title>My Web Page</title>
</head>
<body>
  <h1>Welcome to my Web Page</h1>
  <p>This is some text.</p>
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ul>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

# h1_tag = soup.find('h1')

# print(h1_tag.text)

ul_tag = soup.find('ul')
items = ul_tag.find_all('li')

for item in items:
    print(item.text)



html_doc = """
<html>
<head>
  <title>My Web Page</title>
</head>
<body>
  <h1>Welcome to my Web Page</h1>
  <p class="myclass">This is some text.</p>
  <ul>
    <li class="myclass">Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ul>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

p_tag = soup.find('p', class_='myclass')
li_tags = soup.find_all('li', class_='myclass')

print(p_tag.text)

for li in li_tags:
    print(li.text)

url = 'https://cbseacademyplus.online/'
response = requests.get(url)
html_content = response.text
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get(url, params=params)
auth = ('username', 'password')
response = requests.get(url, auth=auth)

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f'HTTP error occurred: {err}')
except Exception as err:
    print(f'Other error occurred: {err}')




html_doc = """
<html>
<head>
	<title>University Courses</title>
</head>
<body>
	<h1>University Courses</h1>
	<h2>Computer Science</h2>
	<ul>
		<li>Introduction to Programming</li>
		<li>Data Structures and Algorithms</li>
		<li>Operating Systems</li>
	</ul>
	<h2>Mathematics</h2>
	<ul>
		<li>Calculus I</li>
		<li>Linear Algebra</li>
		<li>Differential Equations</li>
	</ul>
	<h2>History</h2>
	<ul>
		<li>World History I</li>
		<li>World History II</li>
		<li>US History</li>
	</ul>
</body>
</html>
"""


"""  use the beautifulsoup library to extract the list of courses from the HTML code and print them in a structured format. """

from bs4 import BeautifulSoup

# Create BeautifulSoup object
soup = BeautifulSoup(html_doc, 'html.parser')

# Extract courses from the HTML code
courses = {}
for h2 in soup.find_all('h2'):
    category = h2.text
    course_list = []
    for li in h2.find_next_sibling('ul').find_all('li'):
        course_list.append(li.text)
    courses[category] = course_list

# Print list of courses
for category, course_list in courses.items():
    print(f"{category}: {', '.join(course_list)}")

"""  use the beautiful library with url to extract the list of courses from the HTML code and print them in a structured format. """
import requests
from bs4 import BeautifulSoup

# Send a GET request to the Wikipedia page for Python programming language and get the HTML response
# url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
url = "https://cbseacademyplus.online/"
response = requests.get(url)

# Parse the HTML response using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the paragraphs on the page and extract their text
paragraphs = soup.find_all("p")
for paragraph in paragraphs:
    text = paragraph.get_text().strip()
    print(text)

