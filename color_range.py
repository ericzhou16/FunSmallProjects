import cv2
import numpy as np


def nothing(x):
    pass


# Load image
image = cv2.imread('1.jpg')

# Create a window
cv2.namedWindow('image')

# Create trackbars for color change
# Hue is from 0-179 for Opencv
cv2.createTrackbar('yMin', 'image', 0, 255, nothing)
cv2.createTrackbar('CrMin', 'image', 0, 255, nothing)
cv2.createTrackbar('CbMin', 'image', 0, 255, nothing)
cv2.createTrackbar('yMax', 'image', 0, 255, nothing)
cv2.createTrackbar('CrMax', 'image', 0, 255, nothing)
cv2.createTrackbar('CbMax', 'image', 0, 255, nothing)

# Set default value for Max HSV trackbars
cv2.setTrackbarPos('yMax', 'image', 255)
cv2.setTrackbarPos('CrMax', 'image', 255)
cv2.setTrackbarPos('CbMax', 'image', 255)

# Initialize HSV min/max values
yMin = CrMin = CbMin = yMax = CrMax = CbMax = 0
while 1:
    # Get current positions of all trackbars
    yMin = cv2.getTrackbarPos('yMin', 'image')
    CrMin = cv2.getTrackbarPos('CrMin', 'image')
    CbMin = cv2.getTrackbarPos('CbMin', 'image')
    yMax = cv2.getTrackbarPos('yMax', 'image')
    CrMax = cv2.getTrackbarPos('CrMax', 'image')
    CbMax = cv2.getTrackbarPos('CbMax', 'image')

    # Set minimum and maximum HSV values to display
    lower = np.array([yMin, CrMin, CbMin])
    upper = np.array([yMax, CrMax, CbMax])
    # print("lower", lower)
    # print("upper", upper)

    # Convert to HSV format and color threshold
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    # print(ycrcb)
    mask = cv2.inRange(ycrcb, lower, upper)
    result = cv2.bitwise_or(image, image, mask=mask)
    # Display result image
    cv2.imshow('image', result)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
