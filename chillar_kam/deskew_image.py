import cv2
import numpy as np

def deskew(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

    # Find the angle of the dominant line
    angles = []
    for line in lines:
        rho, theta = line[0]
        if abs(theta - np.pi/2) > 0.1: # Filter out horizontal lines
            angles.append(theta)
    angle = np.median(angles)

    # Rotate the image to straighten it
    rows, cols = image.shape[:2]
    matrix = cv2.getRotationMatrix2D((cols/2, rows/2), angle*180/np.pi, 1)
    rotated = cv2.warpAffine(image, matrix, (cols, rows), flags=cv2.INTER_CUBIC)

    return rotated

# Load an image
image = cv2.imread('246.jpg')

# Deskew the image
deskewed_image = deskew(image)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Deskewed Image', deskewed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
