import cv2
import numpy as np
import time

#Reading the local file url in string format
src = input("enter the local path of the image the you want to resize: ")
#Reading the image using opencv library
img_old = cv2.imread(rf"{src}", cv2.IMREAD_UNCHANGED)

#Reading the dimensions of the image and printing the same
height, width, no_of_channels = img_old.shape
print("The size of the original image is : ", height, "x", width, "(height x width)")
time.sleep(1)

#Taking the input of desired size of the image from user
scale = int(input("Enter how much percentage that you want to resize your image, example-50 (decreases by 50%), 200(increases by 200%) : "))
scale = scale/100
#Resizing the image by using opencv resize() method
scaled_image = cv2.resize(img_old, (int(scale*width), int(scale*height)), interpolation= cv2.INTER_LINEAR)

#Storing the resized image 
cv2.imwrite('newimage.jpg', scaled_image)
cv2.waitKey(0)
print("The resized image has been stored as 'newimage' !")
