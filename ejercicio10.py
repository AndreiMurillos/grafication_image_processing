import numpy as np
import pandas as pd
import cv2
from PIL import Image
from IPython.display import display
from matplotlib import pyplot as plt

ruta_imagenes = "C:/Users/carli/Documents/ExamenTarea2/imagenes/"

# lista con las rutas completas de las imágenes
imagenes_alineadas = [ruta_imagenes + "turtle-9.bmp", ruta_imagenes + "fish-9.bmp"]

array_pixeles = np.zeros([len(imagenes_alineadas), len(imagenes_alineadas), 3])

for i in range(len(imagenes_alineadas)):
    for j in range(i, len(imagenes_alineadas)):
        imagen1 = np.asarray(Image.open(imagenes_alineadas[i]).convert("1"))
        imagen2 = np.asarray(Image.open(imagenes_alineadas[j]).convert("1"))
        centro1 = np.rint(np.asarray(np.where(imagen1)).mean(axis=1)).astype(int)
        centro2 = np.rint(np.asarray(np.where(imagen2)).mean(axis=1)).astype(int)

        # Alinear el centro de masa de la imagen más chica con el centro de masa de la más grande
        if imagen1.shape[0] * imagen1.shape[1] > imagen2.shape[0] * imagen2.shape[1]:
            filas_extra = imagen1.shape[0] - imagen2.shape[0]
            columnas_extra = imagen1.shape[1] - imagen2.shape[1]
            imagen_ampliada = np.pad(
                imagen2, ((0, filas_extra), (0, columnas_extra)), "constant"
            )

            desplazamiento = centro1 - centro2
            imagen_centrada = np.roll(imagen_ampliada, desplazamiento, axis=(0, 1))
            referencia = imagen1
        else:
            filas_extra = imagen2.shape[0] - imagen1.shape[0]
            columnas_extra = imagen2.shape[1] - imagen1.shape[1]
            imagen_ampliada = np.pad(
                imagen1, ((0, filas_extra), (0, columnas_extra)), "constant"
            )

            desplazamiento = centro2 - centro1
            imagen_centrada = np.roll(imagen_ampliada, desplazamiento, axis=(0, 1))
            referencia = imagen2

        pc = np.count_nonzero(np.logical_and(imagen_centrada, referencia))
        pmas = np.count_nonzero(imagen1) - pc
        pmenos = np.count_nonzero(imagen2) - pc
        array_pixeles[i, j, 0] = pc
        array_pixeles[i, j, 1] = pmas
        array_pixeles[i, j, 2] = pmenos
        array_pixeles[j, i, 0] = pc
        array_pixeles[j, i, 1] = pmenos
        array_pixeles[j, i, 2] = pmas


# crear tabla
tabla_pixeles = pd.DataFrame.from_records(array_pixeles)
display(tabla_pixeles)
