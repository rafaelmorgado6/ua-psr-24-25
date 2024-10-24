import cv2
import argparse

def main():

    parser = argparse.ArgumentParser(description="Exibe uma imagem especificada pelo usuário.")
    parser.add_argument('image', help="Imagem a ser carregada")  # Adicionar argumento de caminho da imagem)
    args = parser.parse_args()  # Interpretação dos argumentos

    image_filename = f'/home/rafa/Desktop/ua-psr-24-25/Parte_05/imagens/{args.image}'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    if image is None:
        print(f"Erro: Não foi possível carregar a imagem '{image_filename}'. Verifique o caminho.")
        return
    
    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()