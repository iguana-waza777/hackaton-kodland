# Clasificador de Residuos por Imagenes + Discord Bot

Un bot inteligente de Discord que **clasifica residuos automáticamente a partir de imágenes** enviadas por los usuarios. El bot detecta si el objeto es **orgánico, reciclable o no reciclable**, promoviendo así una cultura ecológica y la correcta disposición de los desechos.

---

## 🌍 Objetivo

El proyecto busca **reducir la contaminación ambiental** ayudando a las personas a identificar rápidamente el tipo de residuo que están desechando, utilizando **visión por computadora** e inteligencia artificial, todo dentro de la comodidad de un canal de Discord.

---

## 🧰 Tecnologías Utilizadas

- 🐍 **Python 3.10+**
- 🤖 **Discord.py** (para crear el bot)
- 📷 **OpenCV** (procesamiento de imagen)
- 🧠 **TensorFlow / Keras** (modelo de clasificación de residuos)
- 🖼️ **Modelo preentrenado o personalizado** (basado en Google teachable machine)
- 📄 **pillow** (para eliminar el fondo u otros objetos que puedan interferir en la visualisacion por ordenador)
 

---

##📦 Requisitos

Antes de ejecutar el proyecto, asegurate de tener instalados:

- "discord.py"
- "opencv-python"
- "tensorflow"
- "pillow"
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
📦 clasificabot
├── 📁 model               # Modelo de IA entrenado (.h5)
├── 📁 bot                 # Código del bot de Discord
│   └── bot.py
├── 📁 images              # Imágenes de prueba
├── README.md
└── main.py               # Punto de inicio
```
## 📜 Comandos del Bot
A continuación se presentan los comandos disponibles en el bot de Discord y su función dentro del proyecto:

| Comando               | Uso                                      | Descripción                                                                  |
|-----------------------|------------------------------------------|------------------------------------------------------------------------------|
| `!clasificar`         | `/clasificar [adjuntar imagen]`          | Clasifica la imagen adjuntada como reciclable, orgánica o no reciclable.     |
| `!ayuda`              | `/ayuda`                                 | Muestra el listado de comandos disponibles y su uso.                         |
| `!consejo`            | `/consejo`                               | Envía un consejo ecológico aleatorio.                                        |

---









  
