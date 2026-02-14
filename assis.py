import datetime
import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import tkinter as tk
from threading import Thread
import requests
import json
import subprocess
import sys
import re
from datetime import timedelta

class DesktopAssistant:
    def __init__(self):
        # Initialize text-to-speech
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 0.9)
        except Exception as e:
            print(f"Text-to-speech initialization failed: {e}")
            sys.exit(1)

        # Wake word
        self.wake_word = "manav"  # Changed to a more neutral wake word
        self.listening = False
        self.reminders = {}

        # API Keys (You'll need to get these)
        self.weather_api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Get from openweathermap.org
        self.news_api_key = "YOUR_NEWSAPI_KEY"  # Get from newsapi.org

        # Create GUI
        self.root = tk.Tk()
        self.root.title("Desktop Assistant")
        self.root.geometry("400x600")
        
        # Display area
        self.display = tk.Text(self.root, height=25, width=40)
        self.display.pack(pady=10)
        
        # Input field
        self.input_field = tk.Entry(self.root, width=40)
        self.input_field.pack(pady=5)
        
        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)
        
        tk.Button(btn_frame, text="Start Listening", command=self.start_listening).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Enter Text", command=self.process_text).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Clear", command=self.clear_display).pack(side=tk.LEFT, padx=5)
        
        self.running = True
        self.history = []

    def speak(self, text):
        """Convert text to speech"""
        try:
            self.display.insert(tk.END, f"Assistant: {text}\n")
            self.display.see(tk.END)
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            self.display.insert(tk.END, f"Error speaking: {e}\n")

    def listen_for_wake_word(self):
        """Continuously listen for the wake word"""
        r = sr.Recognizer()
        while self.running:
            try:
                with sr.Microphone() as source:
                    self.display.insert(tk.END, "Waiting for wake word...\n")
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source, timeout=None)
                    text = r.recognize_google(audio).lower()
                    
                    if self.wake_word in text:
                        self.speak("Yes, I'm listening!")
                        self.listening = True
                        command = self.get_command()
                        self.process_command(command)
                        self.listening = False
                        
            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                self.display.insert(tk.END, f"Speech recognition error: {e}\n")
            except Exception as e:
                self.display.insert(tk.END, f"Listening error: {e}\n")

    def get_command(self):
        """Get voice command after wake word"""
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                self.display.insert(tk.END, "Listening for command...\n")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5)
                said = r.recognize_google(audio)
                self.display.insert(tk.END, f"You said: {said}\n")
                return said.lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I couldn't understand what you said")
            return ""
        except sr.RequestError as e:
            self.speak(f"Speech recognition error: {e}")
            return ""
        except Exception as e:
            self.speak(f"Audio error: {e}")
            return ""

    def get_weather(self, city):
        """Get weather information"""
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            if data["cod"] == 200:
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                return f"The weather in {city} is {temp}°C with {desc}"
            else:
                return "Couldn't get weather information"
        except Exception as e:
            return f"Error getting weather: {e}"

    def get_news(self):
        """Get latest news headlines"""
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={self.news_api_key}"
            response = requests.get(url)
            data = response.json()
            if data["status"] == "ok":
                headlines = [article["title"] for article in data["articles"][:3]]
                return "Here are the top news headlines: " + ". ".join(headlines)
            else:
                return "Couldn't get news"
        except Exception as e:
            return f"Error getting news: {e}"

    def set_reminder(self, time_str, message):
        """Set a reminder"""
        try:
            # Parse time (assuming format like "in 5 minutes" or "at 14:30")
            if "in" in time_str:
                minutes = int(re.search(r'\d+', time_str).group())
                reminder_time = datetime.datetime.now() + timedelta(minutes=minutes)
            else:
                time_match = re.search(r'at (\d{1,2}):(\d{2})', time_str)
                if time_match:
                    hour, minute = map(int, time_match.groups())
                    now = datetime.datetime.now()
                    reminder_time = now.replace(hour=hour, minute=minute, second=0)
                    if reminder_time < now:
                        reminder_time += timedelta(days=1)
                else:
                    return "Invalid time format"
            
            self.reminders[reminder_time] = message
            Thread(target=self.check_reminders).start()
            return f"Reminder set for {reminder_time.strftime('%H:%M')} - {message}"
        except Exception as e:
            return f"Error setting reminder: {e}"

    def check_reminders(self):
        """Check and trigger reminders"""
        while self.running:
            now = datetime.datetime.now()
            for time in list(self.reminders.keys()):
                if now >= time:
                    self.speak(f"Reminder: {self.reminders[time]}")
                    del self.reminders[time]
            self.root.after(60000, self.check_reminders)  # Check every minute
            break

    def calculate(self, expression):
        """Perform basic calculations"""
        try:
            # Simple evaluation of mathematical expressions
            result = eval(expression, {"__builtins__": {}})  # Safe evaluation
            return f"The result is {result}"
        except Exception:
            return "Invalid calculation"

    def process_command(self, command):
        """Process all commands"""
        if not command:
            return
            
        self.history.append(command)
        
        # Time and Date
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.speak(f"The current time is {current_time}")
            
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            self.speak(f"Today's date is {current_date}")
            
        # Weather
        elif "weather" in command:
            city = command.replace("weather", "").replace("in", "").strip() or "London"
            self.speak(self.get_weather(city))
            
        # News
        elif "news" in command:
            self.speak(self.get_news())
            
        # Reminders
        elif "remind me" in command or "set reminder" in command:
            parts = command.split("to")
            if len(parts) > 1:
                time_part = parts[0].replace("remind me", "").replace("set reminder", "").strip()
                message = parts[1].strip()
                self.speak(self.set_reminder(time_part, message))
            else:
                self.speak("Please specify what and when to remind you")
                
        # Calculations
        elif "calculate" in command or re.match(r"what is \d.*", command):
            expr = command.replace("calculate", "").replace("what is", "").strip()
            self.speak(self.calculate(expr))
            
        # Application Control
        elif "open browser" in command:
            webbrowser.open("https://www.google.com")
            self.speak("Opening browser")
            
        elif "open notepad" in command:
            subprocess.Popen("notepad.exe")
            self.speak("Opening notepad")
            
        elif "open calculator" in command:
            subprocess.Popen("calc.exe")
            self.speak("Opening calculator")
            
        # Web Search
        elif "search" in command:
            query = command.replace("search", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            self.speak(f"Searching for {query}")
            
        # File Management
        elif "create file" in command:
            filename = command.replace("create file", "").strip() or "new_file.txt"
            with open(filename, "w") as f:
                f.write("New file created")
            self.speak(f"Created file: {filename}")
            
        elif "delete file" in command:
            filename = command.replace("delete file", "").strip()
            if os.path.exists(filename):
                os.remove(filename)
                self.speak(f"Deleted file: {filename}")
            else:
                self.speak("File not found")
                
        elif "create folder" in command:
            foldername = command.replace("create folder", "").strip() or "new_folder"
            os.makedirs(foldername, exist_ok=True)
            self.speak(f"Created folder: {foldername}")
            
        # System Commands
        elif "shutdown" in command:
            self.speak("Shutting down the computer")
            os.system("shutdown /s /t 1")
            
        elif "restart" in command:
            self.speak("Restarting the computer")
            os.system("shutdown /r /t 1")
            
        # Basic Interaction
        elif "hello" in command:
            self.speak("Hello! How can I assist you today?")
            
        elif "history" in command:
            self.speak("Showing command history")
            self.display.insert(tk.END, "Command History:\n" + "\n".join(self.history) + "\n")
            
        elif "exit" in command or "quit" in command:
            self.speak("Goodbye")
            self.running = False
            self.root.quit()
            
        else:
            self.speak("I don't understand that command. Try asking about weather, news, or set a reminder!")

    def process_text(self):
        """Handle text input"""
        command = self.input_field.get().lower()
        if command:
            self.display.insert(tk.END, f"You typed: {command}\n")
            self.input_field.delete(0, tk.END)
            self.process_command(command)

    def clear_display(self):
        """Clear the display area"""
        self.display.delete(1.0, tk.END)

    def start_listening(self):
        """Start the wake word listening thread"""
        if not hasattr(self, 'listen_thread'):
            self.listen_thread = Thread(target=self.listen_for_wake_word)
            self.listen_thread.daemon = True
            self.listen_thread.start()
            self.speak(f"Started listening for wake word '{self.wake_word}'")

    def run(self):
        """Start the assistant"""
        self.speak("Hello! I'm your desktop assistant. Click 'Start Listening' to begin voice commands.")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        """Handle window closing"""
        self.speak("Goodbye")
        self.running = False
        self.root.destroy()

def main():
    try:
        assistant = DesktopAssistant()
        assistant.run()
    except Exception as e:
        print(f"Error starting assistant: {e}")

if __name__ == "__main__":
    main()