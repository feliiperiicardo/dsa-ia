# Usando Pillow e Abrindo uma Imagem para Leitura

# pip install Pillow

from PIL import Image

# Abre a imagem
img = Image.open('images/image01.jpg')
#img.show()

# Salva com nome diferente
#img.save('images/new_image.jpg')

############ Cropping - Extraindo a ROI
# Cria uma tupla com as dimensões
dim = (100, 100, 400, 400)
crop_img = img.crop(dim)

# Mostra a imagem crop
crop_img.show()