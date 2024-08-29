import cv2
import time
import os

# Set the path where images will be saved
save_path = 'nasee\PycharmProjects'

# Create the directory if it doesn't exist


# Open a connection to the camera (0 is the default camera)
cap = cv2.VideoCapture(0)

try:
    count = 0
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()


        # Construct the filename
        filename = os.path.join(save_path, f'image_{count:04d}.png')

        # Save the captured frame to the specified path
        cv2.imwrite(filename, frame)
        print(f'Saved {filename}')

        # Wait for 3 seconds
        time.sleep(3)
        count += 1
except KeyboardInterrupt:
    print("Interrupted by user")

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
