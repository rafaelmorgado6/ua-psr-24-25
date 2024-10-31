import cv2
import pyaudio
import webrtcvad
import wave

def main():
    # Initial setup
    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    # Audio configuration
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Initialize VAD
    vad = webrtcvad.Vad()
    vad.set_mode(1)  # 0: Aggressive filtering, 3: Less aggressive

    # Open stream
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    def is_speech(frame, sample_rate):
        """Detects if the audio frame contains speech."""
        return vad.is_speech(frame, sample_rate)

    def record_audio():
        """Records audio when speech is detected."""
        frames = []
        recording = False

        print("Listening for speech...")

        while True:
            frame = stream.read(CHUNK)

            if is_speech(frame, RATE):
                if not recording:
                    print("Recording started.")
                    recording = True
                frames.append(frame)
            else:
                if recording:
                    print("Silence detected, stopping recording.")
                    break

        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        audio.terminate()

        return frames

    def save_audio(frames, filename="output.wav"):
        """Saves the recorded audio frames to a WAV file."""
        wf = wave.open(filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    # Example usage
    frames = record_audio()
    save_audio(frames)
    print("Audio saved as output.wav")

    while True:
        _, image = capture.read()  # Get an image from the camera
        inverted_image = cv2.flip(image, 1)
        cv2.imshow(window_name, inverted_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()  # Release the camera
    cv2.destroyAllWindows()  # Close the window

if __name__ == '__main__':
    main()
