import cv2

# Load the pre-trained Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the image
img = cv2.imread('test3.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Iterate over detected faces
for (x, y, w, h) in faces:
    # Draw rectangle around the face
    cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)

# Display the image with detected faces
cv2.imshow('img', img)
cv2.waitKey()

# Save the image with detected faces
cv2.imwrite('face_detected3.jpg', img)