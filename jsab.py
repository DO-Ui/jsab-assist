import win32.win32gui as win32gui
import win32.win32api as win32api
import PIL
from PIL import ImageGrab
import pygetwindow as gw
import pynput
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
import pyautogui

key = KeyboardController()
mouse = MouseController()

dc = win32gui.GetDC(0)
red = win32api.RGB(255, 0, 0)
PlayerColor = (1, 255, 255)
ObstacleColor = (255, 33, 122)

if len(gw.getWindowsWithTitle('JSB')) == 0:
    print("JSB is not detected")
    exit()

JSAB = gw.getWindowsWithTitle('JSB')[0]
JSABHWND = repr(JSAB)
JSABHWND = JSABHWND[17:]
JSABHWND = JSABHWND[:-1]


while True:
    Windowpos = win32gui.GetWindowRect(int(JSABHWND))
    cropped = Windowpos[0], Windowpos[1], Windowpos[2], Windowpos[3]
    cropped = cropped[0] + 8, cropped[1] + 31, cropped[2] - 8, cropped[3] - 8
    screenshot = ImageGrab.grab(bbox=(cropped))
    foundcoords = []

# turns out it is a simple as changing the step size (dont go over like 30-ish)
    for x in range(0, screenshot.width, 15):
        for y in range(0, screenshot.height, 15):
            coordinate = x, y
            PixelColor = screenshot.getpixel(coordinate)
            if PixelColor == PlayerColor:
                foundcoords.append((x, y))

    if len(foundcoords) == 0:
        continue

    arraylen = len(foundcoords)
    arraylen -= 1
    first = foundcoords[0]
    last = foundcoords[arraylen]
    value1, value2, value3, value4 = first[0], first[1], last[0], last[1]
    xpos = value1 + value3
    xpos = xpos // 2
    ypos = value2 + value4
    ypos = ypos // 2
    # print(xpos, ypos)

    xscreenpos = xpos + cropped[0]
    yscreenpos = ypos + cropped[1]

    scanpoint = []

    # def topbound(y):
    #     if y <= 0:
    #         buffervar1 = 0 - y
    #         buffervar1 = abs(buffervar1)
    #         y = y + buffervar1
    #         y += 1
    #     return y

    # def leftbound(x):
    #     if x <= 0:
    #         buffervar2 = 0 - x
    #         buffervar2 = abs(buffervar2)
    #         x = x + buffervar2
    #         x += 1
    #     return x

    # def rightbound(x):
    #     if x >= screenshot.width:
    #         buffervar3 = x - screenshot.width
    #         x = x - buffervar3
    #         x -= 1
    #     return x

    # def bottombound(y):
    #     if y >= screenshot.height:
    #         buffervar4 = y - screenshot.height
    #         y = y - buffervar4
    #         y -= 1

    scanpoint.extend([ypos - 40, ypos - 20, xpos, xpos])  # Scanning above
    scanpoint.extend([xpos - 40, xpos - 20, ypos, ypos]
                     )  # Scanning to the left
    scanpoint.extend([xpos + 40, xpos + 20, ypos, ypos]
                     )  # Scanning to the right
    scanpoint.extend([ypos + 40, ypos + 20, xpos, xpos])  # Scanning below

    scanpoint.extend([ypos - 40, ypos - 20, xpos + 40,
                     xpos + 20])  # 16 - 19 UP RIGHT
    scanpoint.extend([xpos - 40, xpos - 20, ypos + 40, ypos + 20]   # 20 - 23 UP LEFT
                     )
    scanpoint.extend([xpos + 40, xpos + 20, ypos + 40, ypos + 20]   # 24 - 27 BOTTOM RIGHT
                     )
    # 28 - 31 BOTTOM LEFT
    scanpoint.extend([ypos + 40, ypos + 20, xpos - 40, xpos - 20])

    

    for i in range(0, 32):
        if i == 0 and scanpoint[i] <= 0:
            scanpoint[i] = 1
        if i == 1 and scanpoint[i] <= 0:
            scanpoint[i] = 1
        if i == 4 and scanpoint[i] <= 0:
            scanpoint[i] = 1
        if i == 5 and scanpoint[i] <= 0:
            scanpoint[i] = 1
        if i == 8 and scanpoint[i] >= screenshot.width:
            scanpoint[i] = screenshot.width - 1
        if i == 9 and scanpoint[i] >= screenshot.width:
            scanpoint[i] = screenshot.width - 1
        if i == 12 and scanpoint[i] >= screenshot.height:
            scanpoint[i] = screenshot.height - 1
        if i == 13 and scanpoint[i] >= screenshot.height:
            scanpoint[i] = screenshot.height - 1
        if i == 16 and scanpoint[i] <= 0:
            scanpoint[i] = 1
        if i == 17 and scanpoint[i] <= 0:
            scanpoint[i] = 1
        if i == 18 and scanpoint[i] >= screenshot.width:
            scanpoint[i] = screenshot.width - 1
        if i == 19 and scanpoint[i] >= screenshot.width:
            scanpoint[i] = screenshot.width - 1
        if i == 20 and scanpoint[i] <= 0:
            scanpoint[i] = 1
        if i == 21 and scanpoint[i] <= 0:
            scanpoint[i] = 1
        if i == 22 and scanpoint[i] >= screenshot.height:
            scanpoint[i] = screenshot.height - 1
        if i == 23 and scanpoint[i] >= screenshot.height:
            scanpoint[i] = screenshot.height - 1
        if i == 24 and scanpoint[i] >= screenshot.width:
            scanpoint[i] = screenshot.width - 1
        if i == 25 and scanpoint[i] >= screenshot.width:
            scanpoint[i] = screenshot.width - 1
        if i == 26 and scanpoint[i] >= screenshot.height:
            scanpoint[i] = screenshot.height - 1
        if i == 27 and scanpoint[i] >= screenshot.height:
            scanpoint[i] = screenshot.height - 1
        if i == 28 and scanpoint[i] >= screenshot.height:
            scanpoint[i] = screenshot.height - 1
        if i == 29 and scanpoint[i] >= screenshot.height:
            scanpoint[i] = screenshot.height - 1
        if i == 30 and scanpoint[i] <= 0:
            scanpoint[i] = 1
        if i == 31 and scanpoint[i] <= 0:
            scanpoint[i] = 1

    print(scanpoint)

    down = screenshot.getpixel((scanpoint[14], scanpoint[12]))
    up = screenshot.getpixel((scanpoint[2], scanpoint[0]))
    right = screenshot.getpixel((scanpoint[8], scanpoint[10]))
    left = screenshot.getpixel((scanpoint[4], scanpoint[6]))

    down1 = screenshot.getpixel((scanpoint[15], scanpoint[13]))
    up1 = screenshot.getpixel((scanpoint[3], scanpoint[1]))
    right1 = screenshot.getpixel((scanpoint[9], scanpoint[11]))
    left1 = screenshot.getpixel((scanpoint[5], scanpoint[7]))

    cornerUR = screenshot.getpixel((scanpoint[18], scanpoint[16]))
    cornerUL = screenshot.getpixel((scanpoint[20], scanpoint[22]))
    cornerBR = screenshot.getpixel((scanpoint[24], scanpoint[26]))
    cornerBL = screenshot.getpixel((scanpoint[30], scanpoint[28]))

    # print(down, up, right, left)

    if down == (255, 33, 112) or down == (255, 255, 255):
        print("up")
        key.press(Key.up)
        time.sleep(0.07)
        key.release(Key.up)
    if up == (255, 33, 112) or up == (255, 255, 255):
        print("down")
        key.press(Key.down)
        time.sleep(0.07)
        key.release(Key.down)
    if right == (255, 33, 112) or right == (255, 255, 255):
        print("left")
        key.press(Key.left)
        time.sleep(0.07)
        key.release(Key.left)
    if left == (255, 33, 112) or left == (255, 255, 255):
        print("right")
        key.press(Key.right)
        time.sleep(0.07)
        key.release(Key.right)

    if down1 == (255, 33, 112) or down1 == (255, 255, 255):
        print("up")
        key.press(Key.up)
        time.sleep(0.05)
        key.release(Key.up)
    if up1 == (255, 33, 112) or up1 == (255, 255, 255):
        print("down")
        key.press(Key.down)
        time.sleep(0.05)
        key.release(Key.down)
    if right1 == (255, 33, 112) or right1 == (255, 255, 255):
        print("left")
        key.press(Key.left)
        time.sleep(0.05)
        key.release(Key.left)
    if left1 == (255, 33, 112) or left1 == (255, 255, 255):
        print("right")
        key.press(Key.right)
        time.sleep(0.05)
        key.release(Key.right)

    if cornerBL == (255, 33, 112) or cornerBL == (255, 255, 255):
        print("UR")
        key.press(Key.up)
        key.press(Key.right)
        time.sleep(0.05)
        key.release(Key.right)
        key.release(Key.up)
    if cornerBR == (255, 33, 112) or cornerBR == (255, 255, 255):
        print("UL")
        key.press(Key.up)
        key.press(Key.left)
        time.sleep(0.05)
        key.release(Key.left)
        key.release(Key.up)
    if cornerUR == (255, 33, 112) or cornerUR == (255, 255, 255):
        print("BL")
        key.press(Key.down)
        key.press(Key.left)
        time.sleep(0.05)
        key.release(Key.left)
        key.release(Key.down)
    if cornerUL == (255, 33, 112) or cornerUL == (255, 255, 255):
        print("BR")
        key.press(Key.down)
        key.press(Key.right)
        time.sleep(0.05)
        key.release(Key.right)
        key.release(Key.down)

    # mouse.position = (xscreenpos, yscreenpos)

    # win32gui.SetPixel(dc, xscreenpos, yscreenpos, red)

    # win32gui.SetPixel(dc, scanpoint[0], scanpoint[4], red)
    # win32gui.SetPixel(dc, scanpoint2x, scanpoint2y, red)
    # win32gui.SetPixel(dc, scanpoint3x, scanpoint3y, red)
    # win32gui.SetPixel(dc, scanpoint4x, scanpoint4y, red)

    # time.sleep(0.2)
