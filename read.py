from turtle import pos
import cv2 as cv
import numpy as np
import pyautogui
from ahk import AHK
import keyboard

# ahk = AHK()
ahk = AHK(executable_path='C:\\programy\\AutoHotkey.exe')
font = cv.FONT_HERSHEY_SCRIPT_COMPLEX

def rescaleFrame(frame, scale=0.35):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def playVideo(video):
    while True:
        frame = rescaleFrame(video.read())
        cv.imshow('Video', frame)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break

def get_xy_list_from_contour(contours):
    full_dastaset = []
    for contour in contours:
        xy_list=[]
        for position in contour:
            [[x,y]] = position
            xy_list.append([x,y])
        full_dastaset.append(xy_list)
    return full_dastaset



def auto():
    while(True):
        attackLowestHealthMinionOrEnemy()

        cv.waitKey(100)
        
        if keyboard.is_pressed('Esc'):
            print('You Pressed Escape!')
            break

def attackLowestHealthMinionOrEnemy():
    img = cv.cvtColor(np.array(pyautogui.screenshot()), cv.COLOR_BGR2RGB)
    mask = cv.inRange(img, np.array([91, 91, 200]), np.array([91, 91, 200]))
    output = cv.bitwise_and(img, img, mask = mask)
    mask = cv.inRange(img, np.array([24, 36, 148]), np.array([24, 36, 148]))
    output = cv.bitwise_or(output, cv.bitwise_and(img, img, mask = mask))
    grayscale = cv.cvtColor(output, cv.COLOR_BGR2GRAY)

    # _, thresh = cv.threshold(grayscale, 240, 255, cv.THRESH_BINARY)
    _, thresh = cv.threshold(grayscale, 240, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    # print(get_xy_list_from_contour(contours))

    # print(contours[0][1])

    lowest_hp = 300000
    for contour in contours:    
        approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
        x, y, _, _ = cv.boundingRect(contour)
        l = cv.arcLength(contour,True)
        M = cv.moments(contour)
        if l < lowest_hp:
            lowest_hp = l
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

        cv.drawContours(output, [approx], 0, (0, 255, 0), 5)
    
    if x and y:
        position = pyautogui.position()
        # ahk.right_click(cx + 15, cy + 25)
        pyautogui.click(x = cx + 25, y = cy + 45, button='right')
        pyautogui.moveTo(position, _pause=False)
        # ahk.mouse_move(position)


    # DEBUG
    # cv.imshow("AimBot", output)

# keyboard.add_hotkey('CapsLock', print, args = ('Hotkey', 'Detected')) 
keyboard.add_hotkey('s', attackLowestHealthMinionOrEnemy, suppress=True)
# cv.waitKey(1000)
keyboard.wait('ctrl + x')

# >>> import pyautogui

# >>> pyautogui.position()
# (845, 554)


# auto()


# friendly minions
# mask = cv.inRange(img, np.array([208, 149, 77]), np.array([208, 149, 77]))

# mask = cv.inRange(img, np.array([24, 36, 148]), np.array([24, 36, 148]))
# output = cv.bitwise_or(output, cv.bitwise_and(img, img, mask = mask))

# img = np.array(pyautogui.screenshot())

# loop over the boundaries
# for (lower, upper) in boundaries:
#     # create NumPy arrays from the boundaries
#     lower = np.array(lower, dtype = "uint8")
#     upper = np.array(upper, dtype = "uint8")

#     # "ze mask" - find the colors within the specified boundaries and apply
#     mask = cv.inRange(img, lower, upper)
#     output = cv.bitwise_and(img, img, mask = mask)

    # img_gray = cv.cvtColor(output, cv.COLOR_BGR2GRAY)
    # _, thresh = cv.threshold(img_gray, 240, 255, cv.THRESH_BINARY)
    # contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    # for c in contours:
    #     approx = cv.approxPolyDP(c, 0.01 * cv.arcLength(c, True), True)
    #     cv.drawContours(img, [approx], 0, (0, 255, 0), 5)

# show the images
# cv.imshow("Test", np.hstack([img, output]))



# cv.imshow('COLOR_BGR2GRAY', rescaleFrame(img))


# img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# _, thresh = cv.threshold(img, 240, 255, cv.THRESH_BINARY)
# _, thresh = cv.threshold(img_gray, 240, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

# contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

# for c in contours:
#     approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)
#     cv.drawContours(img, [approx], 0, (0, 255, 0), 5)

        # cv.imshow("Shapes", rescaleFrame(np.hstack([img, output])))

# imageCopy = img.copy()

# cv.destroyAllWindows()

# while(True):
#     # img = cv.cvtColor(np.array(pyautogui.screenshot()), cv.COLOR_BGR2GRAY)
#     img = cv.cvtColor(np.array(pyautogui.screenshot()), cv.COLOR_BGR2RGB)
#     cv.imshow('COLOR_BGR2GRAY', rescaleFrame(img))
#     cv.waitKey(1000)
    

# b, g, r = cv.split(img)
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

# cam = cv.VideoCapture(0)
# playVideo(cam)
# cam.release()












# def attackClosestHero():
#     img = cv.cvtColor(np.array(pyautogui.screenshot()), cv.COLOR_BGR2RGB)
#     mask = cv.inRange(img, np.array([24, 36, 148]), np.array([24, 36, 148]))
#     output = cv.bitwise_and(img, img, mask = mask)
#     grayscale = cv.cvtColor(output, cv.COLOR_BGR2GRAY)
#     _, thresh = cv.threshold(grayscale, 240, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
#     contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
#     lowest_hp = 300

#     for contour in contours:
#         x, y, _, _ = cv.boundingRect(contour)
#         l = cv.arcLength(contour, True)
#         M = cv.moments(contour)
#         if M['m00'] != 0:
#             cx = int(M['m10']/M['m00'])
#             cy = int(M['m01']/M['m00'])
#         if l < lowest_hp:
#             lowest_hp = l
#             lowest_hp_x = x
#             lowest_hp_y = y
        

#         # print(f"x: {cx} y: {cy}")

#         # cv.drawContours(output, [approx], 0, (0, 255, 0), 5)
    
#     if x and y:
#         # ahk.right_click(lowest_hp_x + 25, lowest_hp_y + 120)
#         ahk.right_click(cx, cy)

# keyboard.add_hotkey('s', attackClosestHero, suppress=True)

