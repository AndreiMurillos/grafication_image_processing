import cv2
import numpy as np

# Cargar las dos imágenes binarias
img1 = cv2.imread(
    "C:/Users/carli/Documents/ExamenTarea2/imagenes/ray-10.bmp", cv2.IMREAD_GRAYSCALE
)
img2 = cv2.imread(
    "C:/Users/carli/Documents/ExamenTarea2/imagenes/turtle-9.bmp",
    cv2.IMREAD_GRAYSCALE,
)

# Obtener el centro de masa de cada imagen
m1 = cv2.moments(img1)
cx1 = int(m1["m10"] / m1["m00"])
cy1 = int(m1["m01"] / m1["m00"])

m2 = cv2.moments(img2)
cx2 = int(m2["m10"] / m2["m00"])
cy2 = int(m2["m01"] / m2["m00"])

# Superponer las imágenes
rows, cols = img1.shape
M = np.float32([[1, 0, cx1 - cx2], [0, 1, cy1 - cy2]])
img2_aligned = cv2.warpAffine(img2, M, (cols, rows))

# Calcular los píxeles comunes y no comunes
total_pixels = rows * cols
common_pixels = np.sum(img1 & img2_aligned) / 100
positive_pixels = np.sum(img1 | img2_aligned) / 100 - common_pixels
negative_pixels = rows * cols - (common_pixels + positive_pixels)

img_overlay = cv2.addWeighted(img1, 0.5, img2_aligned, 0.5, 0)
cv2.imshow("Imagen superpuesta", img_overlay)
cv2.waitKey(0)

# Imprimir los resultados
dist = ((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2) ** 0.5
print(f"Distancia entre centros de masa: {dist}")
print(f"Pc: {common_pixels}, P+: {positive_pixels}, P-: {negative_pixels}")
