import cv2
import numpy as np

ruta_imagen = "C:/Users/carli/Documents/ExamenTarea2/imagenes/device8-1.bmp"
imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)

ancho, altura = imagen.shape
imagen_con_rectangulos = np.zeros((ancho * 2, altura * 2, 3), dtype=np.uint8)

for x in range(ancho):
    for y in range(altura):
        if imagen[x][y] == 255:
            x_rect = y * 2
            y_rect = x * 2
            ancho_rect = 2
            altura_rect = 2
            cv2.rectangle(
                imagen_con_rectangulos,
                (x_rect, y_rect),
                (x_rect + ancho_rect, y_rect + altura_rect),
                (255, 255, 255),
                1,
            )


cv2.imshow("Imagen con rectángulos", imagen_con_rectangulos)
cv2.waitKey(0)
cv2.destroyAllWindows()
