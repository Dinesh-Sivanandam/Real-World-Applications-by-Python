import cv2 #importing the opencv

img = cv2.imread("galaxy.jpg",1)    #reading the image file by imread method
                                    #argument 1 is given for reading the file in RBG pattern

#resizing the images for our purpose
resixed_image = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Galaxy",resixed_image)  #showing the image using imshow method
cv2.imwrite("Galaxy_resized.jpg",resixed_image) #Writing the image that is changed the dimension
cv2.waitKey(0)  #this method is used for the waiting time
                #0 for pressinf any key (or) we can give any timing seconds

cv2.destroyAllWindows() #destroying or closing the window after the program executes
