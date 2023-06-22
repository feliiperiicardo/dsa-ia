# Leitura da imagem com skimage

# pip install scikit-image

from skimage import io 

# Para fazer a leitura de uma imagem
img = io.imread('images/image02p2.jpg')
io.imshow(img)

# Salvando como um novo arquivo
io.imsave('images/new_image-p2.jpg', img)

#io.show()
