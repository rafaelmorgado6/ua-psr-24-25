import cv2
import numpy as np

def main():

    image_filename = f'/home/rafa/Desktop/ua-psr-24-25/Parte_05/imagens/atlas2000_e_atlasmv.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    if image is None:
        print(f"Erro: Não foi possível carregar a imagem '{image_filename}'. Verifique o caminho.")
        return
    
    # Converter a imagem de BGR para HSV 
    # Hue(cor basica(0 360)) Saturation(0 100) Valor(brilho(0 100))
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_green = np.array([50,100,50]) 
    upper_green = np.array([70,255,255]) 
 
    mask = cv2.inRange(image_hsv,lower_green,upper_green)

    image_red=image.copy()

    image_red[mask>0] = np.array([0, 0, 255])


    cv2.imshow('window', image)  # Display the image
    cv2.imshow('mask', mask)  # Display the image
    cv2.imshow('image_red', image_red)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()