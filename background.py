from urllib import request
import json
import random
import os
import time
json_file_path = 'C:\\Users\\jairc\\Pictures\\node-whatsapp-apirest - copia\\pardy\\back.json'

with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

def queue_prompt(prompt):
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')  # Convert the Python dictionary back to a JSON formatted string to send in the request
    req = request.Request("http://127.0.0.1:8188/prompt", data=data)
    request.urlopen(req)


def check_file(path, increase):
    # Verificar la cantidad inicial de archivos
    initial_count = len(os.listdir(path))
    
    # Guardar el tiempo de inicio
    start_time = time.time()

    while True:
        # Esperar 5 segundos
        time.sleep(5)

        # Verificar la cantidad actual de archivos
        current_count = len(os.listdir(path))

        # Calcular el tiempo transcurrido
        elapsed_time = time.time() - start_time

        # Comparar la cantidad actual con la cantidad inicial más el número esperado
        if current_count >= initial_count + increase:
            print(f"La cantidad de archivos ha incrementado en al menos {increase}.")
            break
        elif elapsed_time >= 50:  # Si han pasado 40 segundos
            print("Error: no se detectaron suficientes archivos nuevos en 40 segundos.")
            break
        else:
            print("Aún no hay suficientes archivos nuevos.")

def generate_random_15_digit_number():
    return random.randint(100000000000000, 999999999999999)

def gen_background(prompt,path,name):
    #path=r"C:\Users\jairc\Downloads\max.jpg"
    random_15_digit_number = generate_random_15_digit_number()
    data["22"]["inputs"]["ckpt_name"]="albedobaseXL_v20.safetensors"
    data["33"]["inputs"]["steps"] = 23
    data["33"]["inputs"]["cfg"] = 5.5
    data["4"]["inputs"]["image"] = path
    data["33"]["inputs"]["noise_seed"] = random_15_digit_number
    data["83"]["inputs"]["text"] = prompt
    data["92"]["inputs"]["filename_prefix"] = name
    
    queue_prompt(data)
    comfyui_path=r"C:\Users\jairc\Pictures\ComfyUI\output"
    check_file(comfyui_path, 1)
    print("comfyui")


"""
path=r"C:\Users\jairc\Downloads\max.jpg"
prompt="beatiful clear blue sky, cloud, pixar, wild angle, 4k"
gen_background(prompt,path,"back")
"""