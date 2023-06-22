# GetPixel

from PIL import Image

img = Image.open('images/image01.jpg')

print(f'img.size: {img.size}')
print(f'type(img.size): {type(img.size)}')
# (1280, 720)
# <class 'tuple'>

w, h = img.size
print(f'width: {w}')
print(f'height:{h}')
# width:  1280
# height: 720

print(img.getpixel((100,100)))
