import datetime

now = datetime.datetime.now()
print(f"Current Datetime: {now}")

today = datetime.date.today()
print(f"Current date: {today}")

current_time = now.time()
print(f"Current time : {current_time}")

print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minutes: {now.minute}")
print(f"Second: {now.second}")
print(f"Microsecond: {now.microsecond}")
print(f"Weekday (Monday=0, Sunday=6): {now.weekday()}")

my_date = datetime.date(2023, 10, 27)
print(f"My Date: {my_date}")

my_time = datetime.time(14, 30, 45, 123456)
print(f"My time: {my_time}")

my_datetime = datetime.datetime(2024, 7, 24, 9, 15, 0)
print(f"My datetime: {my_datetime}")

formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"formatted datentime: {formatted_date_time}")

formatted_date = now.strftime("%A, %B %d, %Y")
print(f"formatted date: {formatted_date}")

formatted_time = now.strftime("%I:%M %p")
print(f"Formatted time: {formatted_time}")