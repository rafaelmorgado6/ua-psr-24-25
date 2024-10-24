import cv2
import argparse
import numpy as np

def main():

    image_filename = f'/home/rafa/Desktop/ua-psr-24-25/Parte_05/imagens/atlas2000_e_atlasmv.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    if image is None:
        print(f"Erro: Não foi possível carregar a imagem '{image_filename}'. Verifique o caminho.")
        return
    
    lowerb = np.array([0,80,0]) # Ver na imagem os valores minimos para o caixote verde
    upperb = np.array([40,150,40]) # # Ver na imagem os valores maximos para o caixote verde


    mask = cv2.inRange(image,lowerb,upperb)

    cv2.imshow('window', image)  # Display the image
    cv2.imshow('mask', mask)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()