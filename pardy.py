from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import json
import random
import time
from typing import List, Tuple

from comfyui import gen_imagen
from send import send_image, send_message
from face_analisis import analizar_imagen_y_describir
from background import gen_background

app = FastAPI()

class Usuario(BaseModel):
    mensaje: str
    estado: str
    prompt: str
    path_imagen: str | None

class Message(BaseModel):
    numero: str
    mensaje: str

cola_tareas: List[Tuple[str, str]] = []  # Queue stores path_imagen and numero_usuario
estado_sistema = "libre"

def generate_random_15_digit_number():
    return random.randint(100000000000000, 999999999999999)

def cargar_usuarios():
    try:
        with open('usuarios.json', 'r') as file:
            data = file.read()
            if not data:
                return {"usuarios": {}}
            return json.loads(data)
    except FileNotFoundError:
        return {"usuarios": {}}

def guardar_usuarios(usuarios):
    with open('usuarios.json', 'w') as file:
        json.dump(usuarios, file, indent=4)

def procesar_cola():
    global estado_sistema
    while cola_tareas:
        path_imagen, numero_usuario = cola_tareas.pop(0)
        try:
            imagen_path2 = path_imagen.replace('\\', '\\\\')
            description = analizar_imagen_y_describir(imagen_path2)
        except Exception as e:
            print(f"Error al analizar la imagen: {e}")
            description = "Descripción no disponible"
        procesar_imagen(path_imagen, numero_usuario, description)
    estado_sistema = "libre"

def procesar_imagen(path_imagen, numero_usuario, description):
    prompt = f"{description} cartoon,animated,Traditional hand-drawn animation of my melody character,The character has a large pink bunny ear on the top of his head, he is wearing a pink scarf around his neck and is holding a bouquet of yellow flowers, suggesting a friendly and adorable design."
    random_15_digit_number = generate_random_15_digit_number()
    name = str(random_15_digit_number)
    gen_imagen(prompt, path_imagen, name)
    gen_path = rf"C:\Users\jairc\Pictures\ComfyUI\output\{name}_00001_.png"
    back="beatiful clear blue sky, cloud, pixar, wild angle, 4k"
    gen_background(back,gen_path,name)

    intentos = 0
    while intentos < 5:
        try:
            send_image(numero_usuario, gen_path)
            send_message(numero_usuario, "La imagen ha sido procesada")
            break
        except Exception as e:
            intentos += 1
            time.sleep(5)

    if intentos == 5:
        send_message(numero_usuario, "No se pudo enviar la imagen después de varios intentos.")

@app.post("/webhook")
def read_webhook(item: Message):
    global estado_sistema
    usuarios = cargar_usuarios()

    if item.numero not in usuarios["usuarios"]:
        usuarios["usuarios"][item.numero] = {"mensaje": item.mensaje, "estado": "libre", "prompt": "", "path_imagen": None}

    usuario_info = usuarios["usuarios"][item.numero]
    usuario_info["mensaje"] = item.mensaje

    numero_usuario = item.numero.replace("@c.us", "")

    if "Archivo recibido:" in item.mensaje:
        path_imagen = item.mensaje.split("Archivo recibido: ")[1]

        if os.path.exists(path_imagen):
            usuario_info["estado"] = "ocupado"
            usuario_info["path_imagen"] = path_imagen

            if estado_sistema == "libre":
                estado_sistema = "ocupado"
                try:
                    send_message(numero_usuario, "Imagen recibida, espere un momento.")
                except Exception as e:
                    print(f"Error: {e}")
                cola_tareas.append((path_imagen, numero_usuario))
                procesar_cola()
            else:
                cola_tareas.append((path_imagen, numero_usuario))
        else:
            usuario_info["path_imagen"] = None
            send_message(numero_usuario, "Archivo no encontrado.")
    else:
        send_message(numero_usuario, "Envía una imagen para generar")

    guardar_usuarios(usuarios)
    return {"received": True, "usuario_actualizado": item.numero}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
