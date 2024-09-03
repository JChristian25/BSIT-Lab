import time
import random
import sys

ROWS = 10
COLS = 40
arr = [[0 for _ in range(COLS)] for _ in range(ROWS)]

def checkState():
    for r in range(ROWS - 2, -1, -1): 
        for c in range(COLS):
            if arr[r][c] == 1:    
                checkB = arr[r + 1][c]
                checkR = arr[r + 1][c + 1] if c + 1 < COLS else -1
                checkL = arr[r + 1][c - 1] if c - 1 >= 0 else -1
                if checkB == 0:
                    arr[r][c] = 0
                    arr[r + 1][c] = 1
                elif checkL == 0:
                    arr[r][c] = 0
                    arr[r + 1][c - 1] = 1
                elif checkR == 0:
                    arr[r][c] = 0
                    arr[r + 1][c + 1] = 1

def setSand():
    rr = random.randint(0, 0) 
    rc = random.randint(0, COLS - 1)
    if arr[rr][rc] != 1: 
        arr[rr][rc] = 1

def render():
    sys.stdout.write("\033[H")  
    for row in arr:
        sys.stdout.write(''.join("X" if item == 1 else "/" for item in row) + "\n")
    sys.stdout.flush()

def loop():
    sys.stdout.write("\033[2J")  
    sand_timer = time.time()  
    while True:
        current_time = time.time()
        if current_time - sand_timer >= 0.4:
            setSand()
            sand_timer = current_time  
        checkState()  
        render()      
        time.sleep(0.1)  
loop()
