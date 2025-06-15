import pyttsx3
import re

def eliminar_emojis(texto):
    # Patrón más completo para eliminar emojis
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # Emoticonos
        u"\U0001F300-\U0001F5FF"  # Símbolos y pictogramas
        u"\U0001F680-\U0001F6FF"  # Transporte y mapas
        u"\U0001F1E0-\U0001F1FF"  # Banderas
        u"\U00002700-\U000027BF"  # Símbolos adicionales
        u"\U0001F900-\U0001F9FF"  # Emojis adicionales
        u"\U00002600-\U000026FF"  # Símbolos misceláneos
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', texto)

def generar_audio(texto, ruta_salida):
    texto_limpio = eliminar_emojis(texto)
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.save_to_file(texto_limpio, ruta_salida)  # Aquí se corrige el uso de save_to_file
    engine.runAndWait()
