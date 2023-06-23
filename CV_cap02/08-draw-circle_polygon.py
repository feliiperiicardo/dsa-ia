# Desenhando um círculo

import numpy as np 
from skimage import io, draw 

# Leitura
img = np.zeros((100, 100), dtype=np.uint8)

# Desenha um círculo
#x, y = draw.circle_perimeter(50, 50, 10)

# Criando uma imagem vazia e desenhando um polígono
r = np.array([10, 25, 80, 50])
c = np.array([10, 60, 40, 10])
x, y = draw.polygon(r, c)

img[x, y] = 1

io.imshow(img)
io.show()
