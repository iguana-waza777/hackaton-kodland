import discord
from discord.ext import commands
import os
import uuid

from bot.classifier import clasificar_imagen
from bot.voice_response import generar_audio

@commands.command(name="clasificar")
async def clasificar(ctx, modo: str = "texto"):
    if not ctx.message.attachments:
        await ctx.send("📎 Por favor, adjunta una imagen del residuo.")
        return

    imagen = ctx.message.attachments[0]
    nombre_archivo = f"{uuid.uuid4()}.jpg"
    ruta_guardado = f"images/{nombre_archivo}"
    await imagen.save(ruta_guardado)

    categoria, color_tacho, confianza = clasificar_imagen(ruta_guardado)

    mensaje = (
        f"🔍 **Clasificación del residuo:**\n"
        f"🗂️ Categoría: {categoria.capitalize()}\n"
        f"🗑️ Tacho: {color_tacho}\n"
        f"📊 Confianza: {confianza:.2f}%"
    )

    if modo.lower() == "voz":
        ruta_audio = "images/respuesta.mp3"
        generar_audio(mensaje, ruta_audio)
        await ctx.send("🔊 Aquí tienes la respuesta en audio:")
        await ctx.send(file=discord.File(ruta_audio))
        os.remove(ruta_audio)
    else:
        await ctx.send(mensaje)
        
