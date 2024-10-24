import cv2
import numpy as np

white_image = None  # Definir a imagem como global
brush_size = 5  # Tamanho do pincel
current_color = [0,0,0]

def mouse_handler(event, x, y, flags, params):
    global white_image # Usar a variável global 'image'
    global current_color

    if event == cv2.EVENT_LBUTTONDOWN:
        # Desenhar um círculo onde o clique ocorreu
        for i in range(-brush_size, brush_size + 1):
            for j in range(-brush_size, brush_size + 1):
                    white_image[y + i, x + j] = current_color  # Definindo a cor do pixel para verde
        cv2.imshow('window', white_image)

def main():
    global white_image  # Usar a variável global 'image'

    # Criar uma imagem branca de 600x400
    white_image = np.full((400, 600, 3), 255, dtype=np.uint8)  # Formato (altura, largura, canais)

    # Exibir a imagem
    cv2.imshow('window', white_image)

    # Definir o callback de mouse para a janela
    cv2.setMouseCallback('window', mouse_handler)

    while True:
        key = cv2.waitKey(1)  # Esperar por uma tecla
        if key == ord('r'):  # Tecla 'r' para vermelho
            global current_color
            current_color = [0, 0, 255]  # Definindo a cor para vermelho
        elif key == ord('g'):  # Tecla 'g' para verde
            current_color = [0, 255, 0]  # Definindo a cor para verde
        elif key == ord('b'):  # Tecla 'b' para azul
            current_color = [255, 0, 0]  # Definindo a cor para azul
        elif key == 27:  # Tecla ESC para sair
            break
    cv2.destroyAllWindows()  # Fechar todas as janelas

if __name__ == '__main__':
    main()