## Dataset

The dataset contains color 25,000 images with 5 classes of 5,000 images each. All
images are 768 x 768 pixels in size and are in jpeg file format., the main folder
lung_colon_image_set contains two subfolders: colon_image_sets and lung_image_sets.

The subfolder colon_image_sets contain two secondary subfolders: colon_aca
subfolder with 5000 images of colon adenocarcinomas and colon_n subfolder with
5000 images of benign colonic tissues.

The subfolder lung_image_sets contain three secondary subfolders: lung_aca
subfolder with 5000 images of lung adenocarcinomas, lung_scc subfolder with
5000 images of lung squamous cell carcinomas, and lung_n subfolder with 5000
images of benign lung tissues.

We dealt with each type of cancer individually, we use splitfolders function to split
the data folders to train, test, and validation,with ratios of 70%, 20%, 10%

![Dataset](https://i.gyazo.com/2dc0dded94d10066b3b9815fb7261188.png)


Dataset : [kaggle](https://www.kaggle.com/andrewmvd/lung-and-colon-cancer-histopathological-images)

## How To Run ?

1. install requirements.txt using python on cmd

2. cd ..\FastAPI\service 

3. python server.py

4. http://127.0.0.1:8000/docs 

## Screenshots
**Lung FastAPI**

![lungAPI](https://i.gyazo.com/b8676a7ca5d1b469216994c9caaec675.png)

**Colon FastAPI**

![ColonAPI](https://i.gyazo.com/93bd43fa0be20fcd8850bb412453a1b2.png)

