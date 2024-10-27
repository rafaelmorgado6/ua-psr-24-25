#!/usr/bin/env python
import cv2

def main():
    # initial setup
    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
    
    while True:
        _, image = capture.read()  # get an image from the camera

        inverted_image = cv2.flip(image, 1)
        cv2.imshow(window_name, inverted_image)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    capture.release()  # Release the camera
    cv2.destroyAllWindows()  # Close the window
if __name__ == '__main__':
    main()