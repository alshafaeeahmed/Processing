import cv2
import sys
import os
import numpy as np


# function that process each image
def extract_text(input_directory, output_directory, file_name):
    # save the income from the input_directory to 'image'
    image = cv2.imread(os.path.join(input_directory, file_name))
    # result = image.copy()
    # converting image into its hsv form
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Calculate what is the representation of yellow color in the HSV model
    lower = np.array([21, 0, 0])
    upper = np.array([179, 255, 209])
    # creating mask for image segmentation
    mask = cv2.inRange(image, lower, upper)
    # extracting the foreground from the image
    result = cv2.bitwise_and(image, image, mask=mask)
    result = cv2.bitwise_not(result)
    # saving the extracted image
    cv2.imwrite(os.path.join(output_directory, file_name), result)
    # print the result
    print("Created Image: " + os.path.join(output_directory, file_name))


# the main
if __name__ == "__main__":
    # check if the input is correct , if not print suitable sentence
    if len(sys.argv) < 3:
        print("Missing Input/Output Directories!")
    else:
        # print the income Directories
        print("Input Directory:" + sys.argv[1])
        print("Output Directory:" + sys.argv[2])
        # loop for to run the function and print the result for each image
        for file_name in os.listdir(sys.argv[1]):
            extract_text(sys.argv[1], sys.argv[2], file_name)
