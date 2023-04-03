import cv2
import os

# Especifica la ruta de la carpeta que contiene las imágenes binarias .bmp
folder_path = "C:/Users/carli/Documents/ExamenTarea2/imagenes/"

# Recorre todas las imágenes en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith(".bmp"):
        # Carga la imagen y la convierte a escala de grises
        img = cv2.imread(os.path.join(folder_path, filename), cv2.IMREAD_GRAYSCALE)

        # Calcula el número de píxeles con valor 1
        num_pixels = cv2.countNonZero(img)

        # Imprime el número de píxeles con valor 1 en la imagen
        print(f"La imagen {filename} tiene {num_pixels} píxeles con valor 1.")
