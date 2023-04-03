import cv2
import numpy as np
import matplotlib.pyplot as plt

# cargar imagen binaria
img = cv2.imread("C:/Users/carli/Documents/ExamenTarea2/imagenes/ray-10.bmp", 0)

# obtener contornos de objetos binarios
contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# crear una imagen en blanco del mismo tamaño que la original
contour_img = np.zeros_like(img, dtype=np.uint8)

# dibujar contornos en la imagen en blanco
cv2.drawContours(contour_img, contours, -1, (255, 255, 255), 1)

# verificar si la imagen tiene una forma válida
if contour_img.shape != ():
    # mostrar imagen resultante
    plt.imshow(contour_img, cmap="gray")
    plt.show()
else:
    print("La imagen es inválida.")
