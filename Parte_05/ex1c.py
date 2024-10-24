import cv2
import argparse

def main():

    parser = argparse.ArgumentParser(description="Exibe uma imagem especificada pelo usuário.")
    parser.add_argument('image1', help="Imagem a ser carregada")  # Adicionar argumento de caminho da imagem)
    parser.add_argument('image2', help="Imagem a ser carregada")  # Adicionar argumento de caminho da imagem)
    args = parser.parse_args()  # Interpretação dos argumentos

    image_filename1 = f'/home/rafa/Desktop/ua-psr-24-25/Parte_05/imagens/{args.image1}'
    image_filename2 = f'/home/rafa/Desktop/ua-psr-24-25/Parte_05/imagens/{args.image2}'
    
    image1 = cv2.imread(image_filename1, cv2.IMREAD_COLOR) # Load an image
    image2 = cv2.imread(image_filename2, cv2.IMREAD_COLOR) # Load an image

    if image1 is None or image2 is None:
        print(f"Erro: Não foi possível carregar uma das imagens")
        return
    
    while True:
        # Exibe a primeira imagem
        cv2.imshow('window', image1)
        cv2.waitKey(3000)  # Aguarda 3 segundos

        # Exibe a segunda imagem
        cv2.imshow('window', image2)
        cv2.waitKey(3000)  # Aguarda 3 segundos
    


if __name__ == '__main__':
    main()