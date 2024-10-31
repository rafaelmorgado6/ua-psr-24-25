import cv2

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


def main():

    #  # Captura vídeo da câmera padrão 
    capture = cv2.VideoCapture(0)
    window_name = 'Press "q" to EXIT'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
     
    while True:

        # Captura de imagem da camara
        _, image = capture.read()  
        
        # Inverte a imagem 
        inverted_image = cv2.flip(image, 1) 
        
        # Detecta rostos na imagem invertida
        faces = detect_bounding_box(inverted_image)

        # Mostra a imagem invertida na janela
        cv2.imshow(window_name, inverted_image)

        # Se a tecla 'q' for pressionada, sai do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    capture.release()  
    cv2.destroyAllWindows()   

if __name__ == "__main__":
    main()