import time
import random

moves = ('U','D','R','L','F','B',
         'U\'','D\'','R\'','L\'','F\'','B\'',
         'U2', 'D2', 'R2', 'L2', 'F2', 'B2')

counter = 0
seconds = 0
minutes = 0
hours = 0
clock = 0

def scramble():
    for i in range(25):
        print(random.choice(moves), end = " ")

def start():
    try:
        while True: 
            global counter, seconds, minutes, hours, clock
            counter += 1
            seconds = counter % 60
            minutes = int(counter / 60) % 60
            hours = int(counter / 3600)
            clock = f"{hours:02}:{minutes:02}:{seconds:02}"
            print(clock)
            time.sleep(1)
    except KeyboardInterrupt:
        print("It took " + clock + " to solve this scramble!")
        pass

print("\nHere is your scramble: ")
scramble()

print("\nPress Ctrl + C to stop the timer!")
input("Please press Enter to begin:")

start()