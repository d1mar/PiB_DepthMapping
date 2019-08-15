"""
ECE196 Depth Mapping Project
Author: Will Chen
Prerequisite: You need to install OpenCV before running this code
The code here is an example of what you can write to print out 'Hello World!'
Now modify this code to process a local image and do the following:
1. Read geisel.jpg
2. Convert color to gray scale
3. Resize to half of its original dimensions
4. Draw a box at the center the image with size 100x100
5. Save image with the name, "geisel-bw-rectangle.jpg" to the local directory
All the above steps should be in one function called process_image()
"""

# TODO: Import OpenCV
import cv2
import numpy as np
# TODO: Edit this function
def process_image():
    #read as grayscale
    img = cv2.imread('../Depth_Mapping_Deployment/geisel.jpg',0)
    width = int(img.shape[1])
    height = int(img.shape[0])
    dim1 = (width, height)
    #print(dim1)    #printing full image dimensions
    #cv2.imshow('image', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    #resize to half its dimensions
    width = int(img.shape[1] * (1/2))
    height = int(img.shape[0] * (1/2))
    dim2 = (width, height) 
    #print(dim2)    #printing resized image dimensions
    resized = cv2.resize(img, dim2)
    #cv2.imshow('Resized img', resized)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    #draw 100x100 box
    cv2.rectangle(resized, (50,33), (150,99), (255,255,255), 5)
    cv2.imshow('rectangle', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #save image to directory
    cv2.imwrite('geisel-bw-rectangle.jpg', resized)
    
    return

# Just prints 'Hello World! to screen.
def hello_world():
    print('Hello World!')
    return

# TODO: Call process_image function.
def main():
    hello_world()
    process_image()
    return


if(__name__ == '__main__'):
    main()
