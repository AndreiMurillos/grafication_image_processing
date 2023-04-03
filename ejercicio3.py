import cv2
import numpy as np

# Cargar imagen original y escalarla
img_original = cv2.imread(
    "C:/Users/carli/Documents/ExamenTarea2/imagenes/deer-1.bmp", cv2.IMREAD_GRAYSCALE
)
img_escala = cv2.resize(img_original, (0, 0), fx=0.5, fy=0.5)

# Calcular momentos de la imagen original y escalada
moments_original = cv2.moments(img_original)
moments_escala = cv2.moments(img_escala)

# Calcular invariantes de escala
p_vals = [0, 1, 2]
q_vals = [0, 1, 2]

for p in p_vals:
    for q in q_vals:
        inv_escala_original = (
            moments_original["m00"] ** (-((p + q) / 2 + 1))
            * moments_original["mu20"] ** (p / 2)
            * moments_original["mu02"] ** (q / 2)
        )
        inv_escala_escala = (
            moments_escala["m00"] ** (-((p + q) / 2 + 1))
            * moments_escala["mu20"] ** (p / 2)
            * moments_escala["mu02"] ** (q / 2)
        )
        print(f"Invariante de escala (p={p}, q={q}):")
        print(f"Antes del escalado: {inv_escala_original}")
        print(f"Después del escalado: {inv_escala_escala}")
