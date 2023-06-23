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

    if altura_img >= altura_figura or largura_img >= largura_figura or fl == True:

        # Obter as dimensões da figura
        altura_img, largura_img = altura_img//4, largura_img//4

        new_size = (altura_img, largura_img)

        # Redimensionar a imagem
        resized_image = cv2.resize(imagem, new_size)

        # Obter as dimensões da figura
        altura_img, largura_img, _ = resized_image.shape

    # Definir a posição da figura na imagem (supondo posição no canto superior esquerdo)
    posicao_x = x
    posicao_y = y

    # Definir as coordenadas da figura na imagem
    inicio_x = posicao_x
    fim_x = posicao_x + largura_figura
    inicio_y = posicao_y
    fim_y = posicao_y + altura_figura

    # Redimensionar o avatar para a mesma forma da região de interesse
    avatar = cv2.resize(imagem, (fim_x - inicio_x, fim_y - inicio_y))

    # Adicionar a figura à imagem
    imagem[inicio_y:fim_y, inicio_x:fim_x] = avatar

    # Exibir a imagem resultante
    cv2.imshow("Imagem com a figura", imagem)
    cv2.imwrite("new_img.png", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return imagem

new = adicionar_avatar("./img/Equipe.png", "./img/goku.png", 0, 0, True)
