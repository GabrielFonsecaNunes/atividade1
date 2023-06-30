import cv2

def adicionar_avatar(img_origin: str, img_add: str, x: int, y: int, fl: bool = False):
    """
    """    
    # Carregar a imagem
    imagem = cv2.imread(img_origin)

    # Carregar a figura que será adicionada
    figura = cv2.imread(img_add, cv2.IMREAD_UNCHANGED)

    # Obter as dimensões da figura
    altura_figura, largura_figura, _ = figura.shape

    # Obter as dimensões da figura
    altura_img, largura_img, _ = imagem.shape

    if altura_figura >= altura_img or largura_figura >= largura_img or fl == True:
        # Obter as dimensões da figura
        largura_figura, altura_figura = largura_figura//5, altura_figura//5

        new_size = (largura_figura, altura_figura)

        # Redimensionar a imagem
        figura = cv2.resize(figura, new_size)

    # Definir a posição da figura na imagem (supondo posição no canto superior esquerdo)
    posicao_x = x
    posicao_y = y

    # Definir as coordenadas da figura na imagem
    inicio_x = posicao_x
    fim_x = posicao_x + largura_figura
    inicio_y = posicao_y
    fim_y = posicao_y + altura_figura

    # Adicionar a figura à imagem
    imagem[inicio_y:fim_y, inicio_x:fim_x] = figura

    # Exibir a imagem resultante
    cv2.imshow("Imagem com a figura", imagem)
    cv2.imwrite("./img/Equipe_avatar.png", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return imagem

def recortar_figura(img: str, board: int, resized: bool, scale: int):
    """
    """
    frame = cv2.imread(img)

    if resized == True:
        largura, altura, _ = frame.shape
        frame = cv2.resize(frame, (largura//scale, altura//scale))
    
    frame = frame[board:-board, board:-board]

    # cv2.imshow("Imagem Recortada", frame)
    cv2.imwrite(filename='./img/avatar1_recortada.jpg', img = frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return frame[board:-board, board:-board]

avatar1_img = recortar_figura(img="./img/avatar2.jpg", board= 48, resized= True, scale = 4)
team_img = adicionar_avatar(img_origin="./img/Equipe.png", img_add=f"./img/avatar1_recortada.jpg", x = 174, y=18, fl=False)

