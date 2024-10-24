import argparse
import cv2
import numpy as np
from functools import partial
import json
import pprint

# Global variables
window_name = 'window - Ex3a'
image_gray = None
alpha_slider_max = 255

currLimits = {
    'B': {'max': 255, 'min': 0},
    'G': {'max': 255, 'min': 0},
    'R': {'max': 255, 'min': 0}
}

def onTrackbar(value, image, isMax=False, channelID='B'):

    if isMax:
        currLimits[channelID]["max"] = value
    else:
        currLimits[channelID]["min"] = value


    lowerBounds = (currLimits['B']["min"], currLimits['G']["min"], currLimits['R']["min"])
    upperBounds = (currLimits['B']["max"], currLimits['G']["max"], currLimits['R']["max"])


    mask = cv2.inRange(image, lowerBounds, upperBounds)
    newImage = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow(window_name, newImage)  # Display the image



def main(image_path):

    image = cv2.imread(image_path, cv2.IMREAD_COLOR) # Load an image

    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)  # Display the image
    

    cv2.createTrackbar("Min R =>", window_name , 0, 255, partial(onTrackbar, image=image, isMax=False, channelID='R'))
    cv2.createTrackbar("Max R =>", window_name , 255, 255, partial(onTrackbar, image=image, isMax=True, channelID='R'))
    cv2.createTrackbar("Min G =>", window_name , 0, 255, partial(onTrackbar, image=image, isMax=False, channelID='G'))
    cv2.createTrackbar("Max G =>", window_name , 255, 255, partial(onTrackbar, image=image, isMax=True, channelID='G'))
    cv2.createTrackbar("Min B =>", window_name , 0, 255, partial(onTrackbar, image=image, isMax=False, channelID='B'))
    cv2.createTrackbar("Max B =>", window_name , 255, 255, partial(onTrackbar, image=image, isMax=True, channelID='B'))
    
    cv2.waitKey(0)

    finalDict = {'limits': currLimits}

    file_name = 'limits.json'
    with open(file_name, 'w') as file_handle:
        print('writing dictionary to file ' + file_name + "\n")
        json.dump(finalDict, file_handle) # d is the dicionary

    pprint.pprint(finalDict)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image_path', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    main(args['image_path'])