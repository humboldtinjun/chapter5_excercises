from time import time
now = time()
days_since_epoch = now // 86400 # 86400 seconds in a day
seconds_today = now % 86400 #gives us how many seconds remain
hours = seconds_today // 3600 # number of seconds in a day
remaining_seconds = seconds_today % 3600 # gives us the leftover seconds
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"Days since January 1, 1970: {int(days_since_epoch)}")
print(f"Current time: {int(hours)}:{int(minutes)}:{int(seconds)}")