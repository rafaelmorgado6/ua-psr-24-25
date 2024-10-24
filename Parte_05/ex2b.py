import cv2
import argparse
import numpy as np

def main():

    parser = argparse.ArgumentParser(description="Exibe uma imagem especificada pelo usuário.")
    parser.add_argument('image', help="Imagem a ser carregada")  # Adicionar argumento de caminho da imagem)
    args = parser.parse_args()  # Interpretação dos argumentos

    image_filename = f'/home/rafa/Desktop/ua-psr-24-25/Parte_05/imagens/{args.image}'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    if image is None:
        print(f"Erro: Não foi possível carregar a imagem '{image_filename}'. Verifique o caminho.")
        return
    
    # Primeiro converter  para escala de cinza
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)

    print(type(image))
    print(image.shape)
      
   # Binarizar usando NumPy
    threshold_value = 128
    image_thresholded = (image_gray > threshold_value) * 255  # Criar imagem binária

    # Converter a imagem binarizada de volta para uint8
    image_thresholded = image_thresholded.astype(np.uint8)

    cv2.imshow('2a', image)  # Display the image
    cv2.imshow('2b', image_thresholded)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()      