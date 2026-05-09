import numpy as np
from keras.models import load_model
from PIL import Image

def get_class(model_path, labels_path, image_path):

    # Cargar modelo
    model = load_model(model_path, compile=False)

    # Cargar labels
    with open(labels_path, "r") as f:
        labels = f.readlines()

    # Crear array
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Abrir imagen
    image = Image.open(image_path).convert("RGB")

    # Redimensionar
    image = image.resize((224,224))

    # Convertir a array
    image_array = np.asarray(image)

    # Normalizar
    normalized_image = (image_array.astype(np.float32) / 127.5) - 1

    # Guardar imagen
    data[0] = normalized_image

    # Predicción
    prediction = model.predict(data)

    index = np.argmax(prediction)

    class_name = labels[index].strip()

    confidence = prediction[0][index]

    return class_name, confidence