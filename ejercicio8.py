from PIL import Image
import numpy as np
import cv2

# Cargar la imagen binaria
img = cv2.imread(
    "C:/Users/carli/Documents/ExamenTarea2/imagenes/deer-1.bmp", cv2.IMREAD_GRAYSCALE
)

# Convertir la imagen en una matriz NumPy y asegurarse de que sea de tipo uint8
img_arr = np.uint8(np.array(img))
print(img_arr.dtype)

# Detección de contornos
contours, hierarchy = cv2.findContours(
    img_arr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
)

# Calcular los momentos y los ejes principales para cada objeto
for contour in contours:
    moments = cv2.moments(contour)
    cx = int(moments["m10"] / moments["m00"])
    cy = int(moments["m01"] / moments["m00"])
    covariance = np.array(
        [[moments["mu20"], moments["mu11"]], [moments["mu11"], moments["mu02"]]]
    )
    _, _, v = np.linalg.svd(covariance)
    angle = np.arctan2(v[0][1], v[0][0])
    rotation_matrix = cv2.getRotationMatrix2D((cx, cy), angle * 180 / np.pi, 1)
    rotated_img = cv2.warpAffine(
        img_arr, rotation_matrix, img_arr.shape[::-1], flags=cv2.INTER_LINEAR
    )

    # Mostrar la imagen rotada para depuración
    cv2.imshow("Imagen Rotada", rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Guardar la imagen rotada
    cv2.imwrite("objeto_rotado.bmp", rotated_img)

# Mostrar la imagen guardada para depuración
img_rotada = Image.open("objeto_rotado.bmp")
# imprimir ejes principales
print("Eje principal 1: ", v[0])
print("Eje principal 2: ", v[1])
