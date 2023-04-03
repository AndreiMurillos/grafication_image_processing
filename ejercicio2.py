from PIL import Image

# Abrir imagen
img = Image.open("C:/Users/carli/Documents/ExamenTarea2/imagenes/turtle-9.gif")

# Contar cantidad de píxeles con valor 1
pixels = img.load()
count = 0
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixels[i, j] == 1:
            count += 1

# Abrir imagen de referencia
ref_img = Image.open("C:/Users/carli/Documents/ExamenTarea2/imagenes/flatfish-1.gif")

# Contar cantidad de píxeles con valor 1
ref_pixels = ref_img.load()
ref_count = 0
for i in range(ref_img.size[0]):
    for j in range(ref_img.size[1]):
        if ref_pixels[i, j] == 1:
            ref_count += 1

# Calcular factor de escala
alpha = ref_count / count

# Redimensionar imagen original
new_size = (int(img.size[0] * alpha), int(img.size[1] * alpha))
new_img = img.resize(new_size)

# Convertir a imagen binaria
new_pixels = new_img.load()
for i in range(new_img.size[0]):
    for j in range(new_img.size[1]):
        if new_pixels[i, j] < 0.5:
            new_pixels[i, j] = 0
        else:
            new_pixels[i, j] = 1

# Guardar imagen redimensionada
new_img.save("new_image.bmp")
print(alpha)
