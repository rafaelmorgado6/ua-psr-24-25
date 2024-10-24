import cv2

def main():
    
    image_filename = '/home/rafa/Desktop/ua-psr-24-25/Parte_06/imagens/atlascar.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    if image is None:
        print(f"Erro: Não foi possível carregar a imagem em '{image_filename}'")
        return

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, 'PSR', (50, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
    cv2.imshow('window', image)  # Display the image

    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()