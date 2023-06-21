# Enhancement da imagem - Muda o Brilho

from PIL import Image
from PIL import ImageEnhance

# Leitura da imagem
img = Image.open('images/image01.jpg')

# Enhancement
# É realizada uma operação matemática nos pixels de grau 2
#enhancer = ImageEnhance.Brightness(img)
#bright_img = enhancer.enhance(2)

# Muda o contraste da imagem
enhancer = ImageEnhance.Contrast(img)
new_img = enhancer.enhance(2)

# Mostra a imagem
#bright_img.show()
new_img.show()
