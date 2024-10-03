# Dataset Overview

This dataset consists of 25,000 color images, categorized into five distinct classes with 5,000 images per class. Each image is 768 x 768 pixels in size and stored in JPEG format. The main directory, `lung_colon_image_set`, contains two subdirectories: `colon_image_sets` and `lung_image_sets`.

- The `colon_image_sets` folder includes:
  - `colon_aca`: 5,000 images of colon adenocarcinoma tissues.
  - `colon_n`: 5,000 images of benign colon tissues.

- The `lung_image_sets` folder includes:
  - `lung_aca`: 5,000 images of lung adenocarcinoma tissues.
  - `lung_scc`: 5,000 images of lung squamous cell carcinoma tissues.
  - `lung_n`: 5,000 images of benign lung tissues.

We processed each cancer type individually and used the `splitfolders` function to split the dataset into training (70%), testing (20%), and validation (10%) sets.

![Dataset](https://i.gyazo.com/2dc0dded94d10066b3b9815fb7261188.png)

Dataset source: [Kaggle - Lung and Colon Cancer Histopathological Images](https://www.kaggle.com/andrewmvd/lung-and-colon-cancer-histopathological-images)

---

## How to Run the Project

1. Install the required packages by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

2. Navigate to the directory where the `server.py` file is located:
   ```bash
   cd /path/to/server.py
   ```

3. Start the server:
   ```bash
   python server.py
   ```

4. Access the API documentation in your browser:
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Screenshots

### Lung API Interface
![LungAPI](https://i.gyazo.com/b8676a7ca5d1b469216994c9caaec675.png)

### Colon API Interface
![ColonAPI](https://i.gyazo.com/93bd43fa0be20fcd8850bb412453a1b2.png)

--- 
