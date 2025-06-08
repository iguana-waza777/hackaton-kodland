# Clasificador de Residuos por Imagenes + Discord Bot

Un bot inteligente de Discord que **clasifica residuos automáticamente a partir de imágenes** enviadas por los usuarios. El bot detecta si el objeto es **orgánico, reciclable o no reciclable**, promoviendo así una cultura ecológica y la correcta disposición de los desechos.

---

## 🌍 Objetivo

El proyecto busca **reducir la contaminación ambiental** ayudando a las personas a identificar rápidamente el tipo de residuo que están desechando, utilizando **visión por computadora** e inteligencia artificial, todo dentro de la comodidad de un canal de Discord.

---

## 🧰 Tecnologías Utilizadas

- 🐍 **Python 3.10+**
- 🤖 **Discord.py** (para crear el bot)
- 🧠 **TensorFlow / Keras** (modelo de clasificación de residuos)
- 🖼️ **Modelo preentrenado o personalizado** (basado en Google teachable machine)
- 📄 **pillow** (para eliminar el fondo u otros objetos que puedan interferir en la visualisacion por ordenador)
 

---

## 📦 Requisitos

Antes de ejecutar el proyecto, asegurate de tener instalados:
tensorflow==2.11.0
pyttsx3==2.90
Pillow==9.3.0
discord.py==2.3.2
python-dotenv==1.0.1
numpy==1.23.5

---

## 🚀 ¿Cómo funciona?

El usuario sube una imagen al canal de Discord.
El bot descarga la imagen automáticamente.
El modelo de IA analiza la imagen.
El bot responde con la categoría del residuo:
    ✅ Reciclable
    🍃 Orgánico
    🚫 No reciclable
---

## 🛠️ Estructura del Proyecto
```bash
PROYECTO_FINAL_PYTHON
├── bot/
│   ├── __pycache__
│   ├── __init__.py
│   ├── bot.py
│   ├── commands.py
│   ├── classifier.py
│   ├── voice_response.py
├── model/
│   └── keras_model.h5
│   └── labels.txt
├── images/
│   └── temp.jpg
├── .env
├── requirements.txt
├── README.md
└── main.py
```
## 📜 Comandos del Bot
A continuación se presentan los comandos disponibles en el bot de Discord y su función dentro del proyecto:

| Comando               | Uso                                      | Descripción                                                                                                  |
|-----------------------|------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| `!clasificar texto`   | `/clasificar [adjuntar imagen]`          | Clasifica la imagen adjuntada como reciclable, orgánica o no reciclable y lo presenta en un mensaje.         |
| `!clasificar voz`     | `/clasificar [adjuntar imagen]`          | Clasifica la imagen adjuntada como reciclable, orgánica o no reciclable en un audio ablado por computadora.  |
| `!ayuda`              | `/ayuda`                                 | Muestra el listado de comandos disponibles y su uso.                                                         |
| `!consejo`            | `/consejo`                               | Envía un consejo ecológico aleatorio.                                                                        |

---


## 🚀 Uso
Ejecuta el bot:


python main.py
En Discord, utiliza el comando /clasificar y adjunta una imagen del residuo.

El bot responderá con la categoría del residuo y el color del tacho correspondiente.

Para recibir la respuesta en formato de voz, utiliza el comando con el parámetro voz.


## 🎨 Categorías y Colores de Tachos (Villa Rica, Perú)
Categoría	Descripción	Color del Tacho
Orgánico	Restos de comida, cáscaras, residuos vegetales	🟢 Verde
Aprovechable	Papel, cartón, vidrio, plástico, metales	🟡 Amarillo
No Aprovechable	Papel higiénico, envolturas contaminadas	⚫ Negro
Peligroso	Pilas, baterías, medicamentos, aceites	🔴 Roj






  
