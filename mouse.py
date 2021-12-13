import time

import pyautogui
start_x =0
start_y = 0

bbox = (start_x, start_y, start_x + 0, start_y +1)

def test_time():
    with mss() as sct:
        t1 = time.time()
        for i in range(100):
            img = sct.grab(bbox)
    t2 = time.time()
    print(t2-t1)

def print_mouse_pos():
    while True:
        print(pyautogui.position())
        time.sleep(1)


print_mouse_pos()
