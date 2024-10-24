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
    
    # Separar os canais B, G e R
    b, g, r = cv2.split(image) 

    # Definir limites de binarização para cada canal
    b_threshold = 50  # pixeis > 50 passam a 255(branco)
    g_threshold = 100
    r_threshold = 150

     # Binarizar cada canal usando os limites especificados
    _, b_bin = cv2.threshold(b, b_threshold, 255, cv2.THRESH_BINARY)
    _, g_bin = cv2.threshold(g, g_threshold, 255, cv2.THRESH_BINARY)
    _, r_bin = cv2.threshold(r, r_threshold, 255, cv2.THRESH_BINARY)

    # Concatenar os canais binarizados de volta em uma imagem RGB
    merged_image = cv2.merge((b_bin, g_bin, r_bin))

    cv2.imshow('2c', merged_image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()