import cv2
import numpy as np

# Leer la imagen binaria
img = cv2.imread(
    "C:/Users/carli/Documents/ExamenTarea2/imagenes/turtle-9.bmp",
    cv2.IMREAD_GRAYSCALE,
)

# Calcular el centro de masa
m = cv2.moments(img)
xc = int(m["m10"] / m["m00"])
yc = int(m["m01"] / m["m00"])
print("Centro de masa: ({}, {})".format(xc, yc))

# Trasladar la imagen original
tx = 10  # desplazamiento en x
ty = 20  # desplazamiento en y
M = np.float32([[1, 0, tx], [0, 1, ty]])
img_traslada = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# Calcular los momentos centrales para p,q = 0,1 y 2
m00 = cv2.moments(img_traslada)["m00"]
m01 = cv2.moments(img_traslada)["m01"]
m10 = cv2.moments(img_traslada)["m10"]
m11 = cv2.moments(img_traslada)["m11"]
m02 = cv2.moments(img_traslada)["m02"]
m20 = cv2.moments(img_traslada)["m20"]

# Mostrar los momentos centrales
print("m00: ", m00)
print("m01: ", m01)
print("m10: ", m10)
print("m11: ", m11)
print("m02: ", m02)
print("m20: ", m20)
