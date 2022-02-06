import cv2 as cv
import numpy as np
import pyautogui
from ahk import AHK

ahk = AHK(executable_path='C:\\programy\\AutoHotkey.exe')


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



def init():
    font = cv.FONT_HERSHEY_SCRIPT_COMPLEX
    while(True):
        img = cv.cvtColor(np.array(pyautogui.screenshot()), cv.COLOR_BGR2RGB)
        
        # mask = cv.inRange(img, np.array([208, 149, 77]), np.array([208, 149, 77]))
        # output = cv.bitwise_or(output, cv.bitwise_and(img, img, mask = mask))

        # mask = cv.inRange(img, np.array([24, 36, 148]), np.array([24, 36, 148]))
        # output = cv.bitwise_or(output, cv.bitwise_and(img, img, mask = mask))

        mask = cv.inRange(img, np.array([91, 91, 200]), np.array([91, 91, 200]))
        output = cv.bitwise_and(img, img, mask = mask)
        grayscale = cv.cvtColor(output, cv.COLOR_BGR2GRAY)
        # _, thresh = cv.threshold(grayscale, 240, 255, cv.THRESH_BINARY)
        _, thresh = cv.threshold(grayscale, 240, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
        contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

        # print(get_xy_list_from_contour(contours))

        # print(contours[0][1])

        for c in contours:
            approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)
            cv.drawContours(output, [approx], 0, (0, 255, 0), 5)
            n = approx.ravel()
            x = n[0]
            y = n[1]
            string = str(x) + " " + str(y) 
            cv.putText(output, string, (x, y - 6), font, 0.4, (0, 255, 255)) 
        
        # ahk.click(x, y)

        # Used to flatted the array containing 
        # the co-ordinates of the vertices. 
        # n = approx.ravel() 
        # i = 0

        # for j in n : 
        #     if(i % 2 == 0): 
        #         x = n[i] 
        #         y = n[i + 1] 

        #         # String containing the co-ordinates. 
        

        #         if(i == 0): 
        #             # text on topmost co-ordinate. 
        #             cv.putText(output, "Arrow tip", (x, y), 
        #                             font, 0.5, (255, 0, 0)) 
        #         else: 
        #             # text on remaining co-ordinates. 
        #             cv.putText(output, string, (x, y), 
        #                     font, 0.5, (0, 255, 0)) 
        #     i = i + 1

        cv.imshow("AimBot", output)
        cv.waitKey(1000)

init()





# mask = cv.inRange(img, np.array([208, 149, 77]), np.array([208, 149, 77]))
# output = cv.bitwise_or(output, cv.bitwise_and(img, img, mask = mask))

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