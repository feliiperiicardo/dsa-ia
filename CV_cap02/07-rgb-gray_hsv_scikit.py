# Convertendo o espaço de cor

from skimage import color, io 

# Leitura
img = io.imread('images/image02p2.jpg')
#img = io.imread('images/image03p2.jpg')

# Convertendo de RGB para Grayscale
#gray_image = color.rgb2gray(img)

#Convertendo de RGB para hsv
hsv_image = color.rgb2hsv(img)

io.imshow(hsv_image)
#io.imshow(gray_image)
io.show()