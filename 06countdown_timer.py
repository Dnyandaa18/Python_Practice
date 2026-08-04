import time

my_time = int(input("Enter the countdown time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60)
    print(f"{minutes:02d}:{seconds:02d}")
    time.sleep(1) #Why one is used here is because we want to wait for 1 second before printing the next number in the countdown. The time.sleep(1) function pauses the execution of the program for 1 second, creating a countdown effect.
print("Time's up!")