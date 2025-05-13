import cv2
import numpy as np

# Load the image
image = cv2.imread('image.jpg')
image = cv2.resize(image, (500, 480))  # Resize for convenience

# Create a mask (Assume manual mask for simplicity)
# This example assumes the foreground is a rectangle (x, y, width, height)
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (200, 150), (600, 450), 255, -1)  # Example ROI

# Blur the image
blurred = cv2.GaussianBlur(image, (51, 51), 0)

# Combine blurred background and original foreground
foreground = cv2.bitwise_and(image, image, mask=mask)
background = cv2.bitwise_and(blurred, blurred, mask=cv2.bitwise_not(mask))
combined = cv2.add(foreground, background)

# Display and save the result
cv2.imshow('Blurred Background', combined)
cv2.imwrite('blurred_background.jpg', combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
