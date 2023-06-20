# Transformação Geométrica

from PIL import Image

# Leitura da Imagem
img = Image.open('images/image01.jpg')

# Rotaciona 90 graus
rotated_img = img.rotate(90)

# Resize
# Os parâmetros significam a quantidade de pixels ...
# na largura x altura
resize_img = img.resize((300, 200))

# Mostra a imagem
resize_img.show()
#rotated_img.show()
