import cv2
import threading
import time

def capturar_imagem():
    # Inicializar a câmera
    camera = cv2.VideoCapture(0)

    # Loop para exibir o vídeo da câmera
    while True:
        # Ler um frame da câmera
        _, frame = camera.read()

        # Exibir o frame
        cv2.imshow("Pressione 'q' para capturar", frame)

        # Verificar se a tecla 'q' foi pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Aguardar 5 segundos
            time.sleep(5)

            # Salvar a imagem capturada
            cv2.imwrite("foto.png", frame)

            break

    # Liberar a câmera e fechar a janela
    camera.release()
    cv2.destroyAllWindows()

# Iniciar uma thread para capturar a imagem
thread = threading.Thread(target=capturar_imagem)
thread.start()
