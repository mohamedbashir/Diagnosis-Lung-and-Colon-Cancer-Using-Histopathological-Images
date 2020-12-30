from tensorflow.keras.preprocessing import image
from tensorflow.python.framework import ops
from tensorflow.keras.models import model_from_json
from PIL import Image
import tensorflow as tf
import numpy as np
import uvicorn
from fastapi import FastAPI, File, UploadFile
from io import BytesIO
from werkzeug.utils import secure_filename


# Import Keras dependencies
ops.reset_default_graph()

app = FastAPI(title='Tensorflow FastAPI  ')


input_shape = (150, 150)


def load_model():
   # Model files
    MODEL_ARCHITECTURE = 'lung_model_adam_20201117_01.json'
    MODEL_WEIGHTS = 'lung_model_adam_20201117_01.h5'

    # Load the model from external files
    json_file = open(MODEL_ARCHITECTURE)
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)

    # Get weights into the model
    model.load_weights(MODEL_WEIGHTS)
    return model


_model = load_model()


def read_image(images_encoded):
    pil_image = Image.open(BytesIO(images_encoded))
    return pil_image


def preprocess(image: Image.Image):

    img = image.resize(input_shape)
    array = np.asfarray(img)
    x = np.expand_dims(array, axis=0)
    test_image = _model.predict_proba(x)
    result = test_image.argmax(axis=-1)

    if result == [2]:
        result = ('Lung squamous cell carcinoma')
    elif result == [0]:
        result = ('Lung Adenocarcinoma')
    elif result == [1]:
        result = ('Lung benign tissue')

        return result
    return str(result).lower()


def predict(image: np.ndarray):
    predication = _model.predict(image)
    if predication == [2]:
        predication = ('Lung squamous cell carcinoma')
    elif predication == [0]:
        predication = ('Lung Adenocarcinoma')
    elif predication == [1]:
        predication = ('Lung benign tissue')

        return predication
    return str(predication).lower()
