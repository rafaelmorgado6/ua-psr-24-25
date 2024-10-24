import cv2

def main():
    
    image_filename = '/home/rafa/Desktop/ua-psr-24-25/Parte_06/imagens/atlascar.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    if image is None:
        print(f"Erro: Não foi possível carregar a imagem em '{image_filename}'")
        return

    cv2.imshow('window', image)  # Display the image

    height, width, c = image.shape
    x = width // 2
    y = height // 2
    
    cv2.circle(image, (x, y), 50, (0, 255, 0), -1)
    cv2.imshow('window', image)


    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()