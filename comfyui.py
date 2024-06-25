from urllib import request
import json
import random
import os
import time
json_file_path = 'oneface.json'

with open(json_file_path, 'r') as json_file:
    
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

def gen_imagen(prompt,path,name):
    #path=r"C:\Users\jairc\Downloads\max.jpg"
    negative = "bad anatomy, bad proportions, blurry, cloned face, cropped, deformed, dehydrated, disfigured, duplicate, error, extra arms, extra fingers, extra legs, extra limbs, fused fingers, gross proportions, jpeg artifacts, long neck, low quality, lowres, malformed limbs, missing arms, missing legs, morbid, mutated hands, mutation, mutilated, out of frame, poorly drawn face, poorly drawn hands, signature, text, too many fingers, ugly, username, watermark, worst quality,naked"
    random_15_digit_number = generate_random_15_digit_number()
    data["411"]["inputs"]["ckpt_name"]="albedobaseXL_v20.safetensors"
    data["550"]["inputs"]["image"] = path
    data["409"]["inputs"]["seed"] = random_15_digit_number
    data["408"]["inputs"]["prompt"] = prompt
    data["570"]["inputs"]["filename_prefix"] = name
    data["409"]["inputs"]["ip_adapter_scale"] = 0.8
    data["409"]["inputs"]["controlnet_conditioning_scale"] = 0.8
    data["409"]["inputs"]["steps"] = 23
    data["409"]["inputs"]["guidance_scale"] = 7
    queue_prompt(data)
    comfyui_path=r"C:\Users\jairc\Pictures\ComfyUI\output"
    check_file(comfyui_path, 1)
    print("comfyui")



#path=r"C:\Users\jairc\Downloads\max.jpg"
#prompt="An male Astronaut in space,a cutting-edge astronaut suit that incorporates advanced technology and materials for a future mission to Mars. Describe its appearance, features, and functionalities in detail, trending on artstatio, full body, shoulders aligned, solid gray background"
#gen_imagen(prompt,path)
#a={'1': 'An illustration of a focused and determined man with long curly hair and a serious expression on his face, holding a quill pen above parchment filled with mathematical symbols.', '2': 'A detailed image displaying planets, moons, and stars in a vast, dark space. A large celestial body hovers in the center with an orbiting ring of smaller bodies around it.', '3': "A cartoon-like image of two people, one holding a bowling ball, and the other falling backwards as if they got hit by it, both in mid-air, symbolizing Newton's third law of motion - action and reaction.", '4': "A realistic depiction of a ball placed on an inclined plane. The ball is steadily rolling downwards, indicating Newton's second law of motion - the force exerted on an object is equal to the mass of that object multiplied by its acceleration.", '5': "A woman with a surprised look on her face as she drops an apple from her hand. The apple is about to hit the ground, emphasizing Newton's famous theory of gravitation and the laws of motion.", '6': "A tall, spiral chart illustrating the mathematical formulas and theories that formed the foundation of Isaac Newton's work in physics. The chart is accompanied by a depiction of Newton himself deep in thought, with his mathematical equations spread out on a table.", '7': "A close-up of Newton's book, 'Mathematical Principles of Natural Philosophy' (also known as 'Principia'), with the image of Isaac Newton in the background. His impact on the world of science and physics is symbolized through the weight of the book, resting on a desk.", '8': "A group of people gathered around a table, discussing the new ideas introduced by Isaac Newton in the field of physics, with one individual sketching the conversation on parchment. This illustrates the spread of Newton's discoveries and their impact on the scientific community."}