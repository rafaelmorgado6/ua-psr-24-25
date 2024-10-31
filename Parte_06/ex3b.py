import cv2
import numpy as np

# Esta é uma classe do OpenCV que permite a detecção de objetos em imagens, 
# neste caso caras devido a "haarcascade_frontalface_default.xml"
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def detect_bounding_box(image):

    # Converte a imagem para tons de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Deteta rostos na imagem 
    faces = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
    
    # Desenha um retângulo ao redor de cada rosto detectado
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return faces


def highlight_edges(image, faces):
    
    # Converte a imagem para escala de cinza para detecção de bordas
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Deteta as bordas da gray_image
    edges = cv2.Canny(gray_image, 100, 200)

    # Cria uma máscara para as áreas das faces (define quais partes de uma imagem devem ser alteradas, analisadas ou mantidas.21)
    mask = np.zeros_like(edges)  # Inicializa a máscara a preto
    for (x, y, w, h) in faces:
        mask[y:y + h, x:x + w] = 255  # Define as áreas das faces na máscara a branco

    # Inverte a máscara para obter áreas fora das faces
    mask_inv = cv2.bitwise_not(mask)

    # Dilata a máscara invertida para cobrir áreas adjacentes
    dilated_mask = cv2.dilate(mask_inv, np.ones((5, 5), np.uint8), iterations=1)

    # Aplica a máscara dilatada na imagem de bordas, obtem nova imagem só com bordas fora da face
    edges_masked = cv2.bitwise_and(edges, edges, mask=dilated_mask)

    # Crie uma imagem vazia do mesmo tamanho que a imagem original mas para bordas coloridas
    colored_edges = np.zeros_like(image)

    # Aplique a cor onde as bordas estão presentes
    colored_edges[edges_masked > 0] = [0, 255, 0]
    
    # Adiciona as bordas detectadas à imagem original
    output_image = cv2.add(image, colored_edges)

    return output_image



def main():
     
    capture = cv2.VideoCapture(0)
    window_name = 'Press "q" to EXIT'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
     
    while True:
        _, image = capture.read()  # get an image from the camera
        
        inverted_image = cv2.flip(image, 1)
        faces = detect_bounding_box(inverted_image)
        output_image = highlight_edges(inverted_image, faces)
        cv2.imshow(window_name, output_image )
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    capture.release()  # Release the camera
    cv2.destroyAllWindows()  # Close the window

if __name__ == "__main__":
    main()


# cv2.Canny() -> Detecta bordas em uma imagem usando o algoritmo de Canny.
#                   -> Deteta as bordas

# cv2.bitwise_not() ->  Inverte os bits de uma imagem ou máscara 
#                       ->  Selecionar zonas que náo estao dentro da face detection

# cv2.dilate() -> Aumenta as áreas brancas em uma imagem binária (máscara).
#                   -> após operações de detecção de bordas ajuda a melhorar a visibilidade das bordas

# cv2.add() -> Adiciona duas imagens pixel a pixel.
#               -> Junta imagem origina e máscara, ficando a imagem original com bordas


