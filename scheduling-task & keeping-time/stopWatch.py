# stopwatch.py - A simple stopwatch program.

import time

# Display the porgram's instructions

print(
    """ \n\nInstructions\n
press Enter to begin.\n
Afterwards press Enter to "click" the stopwatch.\n
Press Ctrl-C to quit"""
)
input()  # press Enter to begin
print("Started")
startTime = time.time()
lastTime = startTime
lapNum = 1

# TODO: start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f"Lap #{lapNum}: {totalTime} {lapTime}", end="")
        lapNum += 1
        lastTime = time.time()  # reset the last lap time

except KeyboardInterrupt:
    # handle the ctrl-c exception to keep its message from displaying.
    print("\nDone")
