import cv2

# the following command allows us to upload an image (BGR - Blue, Green, Red )
# there are multiple ways that you can load an image, below are a few of them
# -1 or cv2.IMGREAD_COLOR wil load an image and ignore the transpant bg (it will upload a coloured image)
# 0 or cv2.IMGREAD_COLOR wil load an image in Grayscale
# 1 or cv2.IMGREAD_UNCHANGED wil load an image in the way that i was saved (will load with the transparrent bg)

img = cv2.imread('assets/logo1.png', 0)

# the following code is used for resizing and manipulating the scale of the image
img = cv2.resize(img, (4000,5000))
# img = cv2.rotate(img, cv2.cv2.ROTATE_180_CLOCKWISE)

# the following allows for writing on an image and saving it as a new one
cv2.imwrite('new_img.png', img)

# this allows us to show the image
cv2.imshow('Image', img)
# this will wait an infinte amount of time before stopping the show, it is measured in seconds so if you pass 5 as an argument it will wait 5 seconds
cv2.waitKey(0)
# 
cv2.destoryAllWindows
