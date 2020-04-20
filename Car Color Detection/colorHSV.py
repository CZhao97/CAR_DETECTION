import  cv2
import numpy as np
import colorList
 
filename='1.jpg'

def get_color(frame):
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    maxsum = -100
    color = None
    color_dict = colorList.getColorList()
    for d in color_dict:
        mask = cv2.inRange(hsv,color_dict[d][0],color_dict[d][1])
        cv2.imwrite(d+'.jpg',mask)
        binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
        binary = cv2.dilate(binary,None,iterations=2)
        cnts, hiera = cv2.findContours(binary.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        sum = 0
        for c in cnts:
            sum+=cv2.contourArea(c)
        if sum > maxsum :
            maxsum = sum
            color = d
 
    return color
 
 

def display_img():
    image = cv2.imread(filename)
    orange = cv2.imread('orange.jpg')
    cyan = cv2.imread('cyan.jpg')
    red = cv2.imread('red.jpg')
    red2 = cv2.imread('red2.jpg')
    white = cv2.imread('white.jpg')
    blue = cv2.imread('blue.jpg')
    black = cv2.imread('black.jpg')
    green = cv2.imread('green.jpg')

    line1 = np.concatenate((image, orange, cyan),axis=1)
    line2 = np.concatenate((red, red2, white), axis=1)
    line3 = np.concatenate((blue, black, green),axis=1)

    images = np.concatenate((line1, line2, line3),axis=0)
    cv2.imshow('Predicted Colors of the Car',images)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    frame = cv2.imread(filename)
    print(get_color(frame))
    
    display_img()