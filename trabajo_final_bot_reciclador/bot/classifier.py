import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array

# Cargar el modelo y las etiquetas
modelo = load_model("model/keras_model.h5")
with open("model/labels.txt", "r", encoding="utf-8") as f:
    etiquetas = [line.strip().split(" ", 1)[-1] for line in f.readlines()]

# Diccionario de colores de tacho por categoría
colores_tacho = {
    "orgánico": "Marrón",
    "aprovechable": "Verde",
    "no aprovechable": "Negro",
    "peligroso": "Rojo"
}

def clasificar_imagen(ruta_imagen):
    img = load_img(ruta_imagen, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    predicciones = modelo.predict(img_array)
    indice_max = np.argmax(predicciones[0])
    confianza = float(predicciones[0][indice_max]) * 100

    etiqueta_cruda = etiquetas[indice_max]
    categoria = etiqueta_cruda.strip().lower()

    # Limpieza de caracteres especiales y número
    for prefijo in ["0", "1", "2", "3"]:
        categoria = categoria.replace(prefijo, "").strip()

    categoria = categoria.replace("ã¡", "á").replace("Ã³", "ó").replace("ã©", "é")

    # Buscar color correspondiente
    color_tacho = colores_tacho.get(categoria, "Desconocido")

    return categoria.capitalize(), color_tacho, round(confianza, 2)
