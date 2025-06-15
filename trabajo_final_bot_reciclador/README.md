Clasificador de Residuos con Discord Bot
Este proyecto consiste en un bot de Discord que clasifica imágenes de residuos en cuatro categorías: Orgánico, Aprovechable, No Aprovechable y Peligroso. Además, indica el color del tacho correspondiente según las normativas de Villa Rica, Perú, y ofrece respuestas en formato de texto o voz.

🎯 Objetivo
Fomentar la correcta segregación de residuos mediante una herramienta interactiva.

Utilizar inteligencia artificial para clasificar residuos a partir de imágenes.

Promover la educación ambiental en comunidades locales.

📁 Estructura del Proyecto

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


🚀 Uso
Ejecuta el bot:


python main.py
En Discord, utiliza el comando /clasificar y adjunta una imagen del residuo.

El bot responderá con la categoría del residuo y el color del tacho correspondiente.

Para recibir la respuesta en formato de voz, utiliza el comando con el parámetro voz.


🎨 Categorías y Colores de Tachos (Villa Rica, Perú)
Categoría	Descripción	Color del Tacho
Orgánico	Restos de comida, cáscaras, residuos vegetales	🟢 Verde
Aprovechable	Papel, cartón, vidrio, plástico, metales	🟡 Amarillo
No Aprovechable	Papel higiénico, envolturas contaminadas	⚫ Negro
Peligroso	Pilas, baterías, medicamentos, aceites	🔴 Rojo