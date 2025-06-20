import cv2

# Carrega a imagem colorida (substitua 'lena.png' pelo nome do seu arquivo)
imagem_colorida = cv2.imread('lena.png')

# Converte a imagem para níveis de cinza
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Aplica binarização com limiar (threshold)
# Aqui usamos 127 como valor de limiar: tudo acima vira 255 (branco); abaixo vira 0 (preto)
_, imagem_binaria = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

# Exibe as imagens
cv2.imshow('Imagem Original', imagem_colorida)
cv2.imshow('Imagem em Cinza', imagem_cinza)
cv2.imshow('Imagem Binária', imagem_binaria)

# Espera o usuário pressionar uma tecla e fecha as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
