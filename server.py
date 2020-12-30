from io import BytesIO
import numpy as np
import tensorflow as tf
import uvicorn
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
from tensorflow.python.framework import ops
from werkzeug.utils import secure_filename
import predict

# Import Keras dependencies
ops.reset_default_graph()

app = FastAPI(title='Tensorflow FastAPI  ')


@app.get("/index")
def hello_world():
    return "Hello World"


@app.post('/api/predict_lung')
def predict_image(file: bytes = File(...)):
    # read the fille uploaded be user
    image = predict.read_image(file)
    # after doing preprocessing
    image = predict.preprocess(image)
    # make prediaction
    print(image)
    return image


if __name__ == "__main__":
    uvicorn.run(app)
