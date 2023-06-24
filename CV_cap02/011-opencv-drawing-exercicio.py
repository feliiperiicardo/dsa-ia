import cv2 
 
imagem = cv2.imread('images/estrada.jpg')

#percorre linhas
for y in range(0, imagem.shape[0], 50): 
	#percorre colunas
	for x in range(0, imagem.shape[1], 50):
	    imagem[y:y+25, x: x+25] = (0,255,255)
	    #print(f'x: {x}, y: {y}')
	    #cv2.imshow("Imagem modificada", imagem) 
	    #cv2.waitKey(0)

# Gerando um círculo no centro da imagem 
(centerX, centerY) = (imagem.shape[1] // 2, imagem.shape[0] // 2)
color = (0,255,255)
radius = 50
cv2.circle(imagem, (centerX, centerY), radius, color, -1)
cv2.circle(imagem, (centerX, centerY), radius//2, (255,255,255), -1)
cv2.circle(imagem, (centerX, centerY), radius//4, (0,0,0), -1)

cv2.imshow("Imagem modificada", imagem) 
cv2.waitKey(0)