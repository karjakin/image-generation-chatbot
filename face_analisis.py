from deepface import DeepFace

def analizar_imagen_y_describir(imagen_path):
    try:
        # Análisis de la imagen con DeepFace
        resultados = DeepFace.analyze(img_path=imagen_path, actions=['age', 'gender', 'race', 'emotion'])
        
        # Asegurándonos de que los resultados se manejan correctamente
        if isinstance(resultados, list):
            # Tomando el primer resultado de la lista
            resultado = resultados[0]
        else:
            # Si es un diccionario, lo usamos directamente
            resultado = resultados
        
        # Construcción del texto descriptivo
        texto_descriptivo = f"A {resultado['dominant_gender']} with {resultado['age']} years old, "
        
        return texto_descriptivo
    except Exception as e:
        # Manejo de errores
        return f""

# Ruta de la imagen a analizar
#imagen_path = r'C:\Users\jairc\Pictures\node-whatsapp-apirest - copia\src\config\wsp\media\media_1706455615219.jpeg'

# Uso de la función para obtener la descripción
#descripcion = analizar_imagen_y_describir(imagen_path)
#print(descripcion)
