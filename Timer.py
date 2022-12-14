import time

my_time = int(input("time to sleep: "))

for x in range(my_time, 0, -1):
    seconds = int(x % 60)
    hour = int(x / 3600)
    minutes = int(x / 60) % 60
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times Up!")