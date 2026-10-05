import cv2
print("Daniel Gallegos NC 1392")
# Cargar la imagen
imagen = cv2.imread("imagenes/koala.webp")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(
    imagen,
    5
)

# Mostrar imágenes
cv2.imshow("Koala original 1392", imagen)
cv2.imshow("Koala filtrado 1392", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "resultados/koala.webp",
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("../resultados/koala.webp")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("Daniel Gallegos NC 1392")