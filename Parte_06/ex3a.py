import cv2

# Esta é uma classe do OpenCV que permite a detecção de objetos em imagens, 
# neste caso caras devido a "haarcascade_frontalface_default.xml"
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def detect_bounding_box(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

# Main function to test face detection
def main():
     
    capture = cv2.VideoCapture(0)
    window_name = 'Press "q" to EXIT'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
     
    while True:
        _, image = capture.read()  # get an image from the camera
        
        inverted_image = cv2.flip(image, 1)
        faces = detect_bounding_box(inverted_image)
        cv2.imshow(window_name, inverted_image)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    capture.release()  # Release the camera
    cv2.destroyAllWindows()  # Close the window
    # Detect faces and draw bounding boxes
    

if __name__ == "__main__":
    main()