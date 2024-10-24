import argparse
import cv2

# Global variables
window_name = 'window - Ex3a'
image_gray = None


def onTrackbar(threshold):
    
    global image_gray # use global var
    
    # Aplicar threshold à imagem em tons de cinza
    _, thresh_img = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)

    # Mostrar a imagem thresholded na janela
    cv2.imshow(window_name, thresh_img)

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    global image_gray # use global var
    
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    
    cv2.namedWindow(window_name)

    # Criar a trackbar
    cv2.createTrackbar('Threshold', window_name, 0, 255, onTrackbar)
    onTrackbar(0)

    # Exibir a imagem original em tons de cinza inicialmente
    cv2.imshow(window_name, image_gray)

    # add code to create the trackbar ...
    cv2.waitKey(0)

if __name__ == '__main__':
    main()