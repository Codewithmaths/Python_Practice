import datetime

current_time = datetime.datetime.now()
current_hour = current_time.hour

if current_hour < 12:
    print("Good morning!")
elif 12 <= current_hour < 18:
    print("Good afternoon!")
else:
    print("Good evening!")