# Leitura, Visualização e Gravação de Imagens
 
# Para executar este script:
# python 09-opencv-read-display-save.py --image images/familia.jpg

# Imports
import argparse
import cv2

# Construindo o analisador de argumentos e analisando os argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Caminho da imagem")
args = vars(ap.parse_args())

# Carregando a imagem e mostrando algumas informações básicas 
image = cv2.imread(args["image"])
print("Altura: {} pixels".format(image.shape[0]))
print("Largura: {} pixels".format(image.shape[1]))
print("Canais: {}".format(image.shape[2]))

# Mostrando a imagem e aguardando uma tecla pressionada para finalizar
cv2.imshow("Image", image)
cv2.waitKey(0) # Espera finalizar com a ação de pressioniar uma tecla

# Salvando uma cópia da imagem
cv2.imwrite("images/nova_familia.jpg", image)