import cv2

def main():

    image_filename = '/home/rafa/Desktop/ua-psr-24-25/Parte_05/imagens/atlascar.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()