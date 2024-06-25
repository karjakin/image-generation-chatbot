import requests

def send_image(numero, filePath):
    url = "http://localhost:3000/envio"
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "numero": numero,
        "filePath": filePath  
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.text)

# Ejemplo de uso
# send_image("5212223632487", "C:/Users/jairc/Pictures/node-whatsapp-apirest - copia/image.png")
        
def send_message(numero, mensaje):
    url = "http://localhost:3000/envio"
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "numero": numero,
        "mensaje": mensaje 
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.text)

# Ejemplo de uso
#send_message("5212223632487", "hola, soy pardy")