from io import BytesIO
import numpy as np
import tensorflow as tf
import uvicorn
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image


app = FastAPI()

### LUNG 

input_shape = (150, 150)


def load_model():
   # Model files
	MODEL_ARCHITECTURE = "lung_model_adam_20201117_01.json"
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


def read_image(file):
	image = Image.open(BytesIO(file))
	return image


def preprocess(image: Image.Image):

	image = image.resize(input_shape)
	array = np.asfarray(image)
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


@app.get("/index")
def hello_world():
	return "Hello World"


@app.post('/lung')
async def predict(file: UploadFile = File(...)):
	extension = file.filename.split(".")[-1] in ("jpeg")
	if not extension:
		return {"result": "Image must be jpeg format!"}
	# read the file uploaded be user
	image = read_image(await file.read())
	# preprocessing
	prediction = preprocess(image)
	# print prediaction
	print(prediction)

	return {"result": prediction}

### COLON

def load_colon_model():
   # Model files
	MODEL_ARCHITECTURE = 'colon_cancer_3.json'
	MODEL_WEIGHTS = 'colon_cancer_3_weights.h5'

	# Load the model from external files
	json_file = open(MODEL_ARCHITECTURE)
	loaded_model_json = json_file.read()
	json_file.close()
	model = model_from_json(loaded_model_json)

	# Get weights into the model
	model.load_weights(MODEL_WEIGHTS)

	return model


colon_model = load_colon_model()


def read_colon_image(file):
	image = Image.open(BytesIO(file))
	return image


def preprocess_colon(image: Image.Image):
	
	colon_img = image.resize(input_shape)
	c_c_img = np.asfarray(colon_img)
	c_c_img = c_c_img/255
	c_c_img = np.expand_dims(c_c_img, axis=0)
	#predict
	diagnosis_colon_cancer= colon_model.predict(c_c_img)

	if diagnosis_colon_cancer>= 0.5:
		result=('I am {:.2%} percent confirmed that this is a benign case'.format(diagnosis_colon_cancer[0][0]))
	else:
		result=('I am {:.2%} percent confirmed that this is a adenocarcinoma case'.format(1-diagnosis_colon_cancer[0][0]))
	return result



@app.post('/colon')
async def predict(file: UploadFile = File(...)):
	extension = file.filename.split(".")[-1] in ("jpeg")
	if not extension:
		return {"result": "Image must be jpeg format!"}
	# read the file uploaded be user
	image = read_colon_image(await file.read())
	# preprocessing
	prediction = preprocess_colon(image)
	# print prediaction
	print(prediction)

	return {"result": prediction}



if __name__ == "__main__":
	uvicorn.run(app)
