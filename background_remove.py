import cv2
import sys
import os
import numpy as np


def extract_text(input_directory, output_directory, file_name):
    image = cv2.imread(os.path.join(input_directory, file_name))
    result = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([21, 0, 0])
    upper = np.array([179, 255, 209])
    mask = cv2.inRange(image, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)
    result = cv2.bitwise_not(result)
    cv2.imwrite(os.path.join(output_directory, file_name), result)
    print("Created Image: " + os.path.join(output_directory, file_name))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Missing Input/Output Directories!")
    else:
        print("Input Directory:" + sys.argv[1])
        print("Output Directory:" + sys.argv[2])
        for file_name in os.listdir(sys.argv[1]):
            extract_text(sys.argv[1], sys.argv[2], file_name)
