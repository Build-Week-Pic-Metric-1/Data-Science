import numpy as np
import requests
from PIL import Image
from io import BytesIO

from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.applications.resnet50 import decode_predictions
from tensorflow.keras.preprocessing import image



def process_img_path(url):
    ''' Processes image url and compresses it to 224 x 224 pixels'''
    if url.startswith('http://') or url.startswith('https://') or url.startswith('ftp://'):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((224, 224))
    else:
        if not os.path.exists(url):
            raise Exception('Input image file does not exist')
        img = image.load_img(url, target_size=(224, 224))
    return img

def resnet_model(img):
    ''' Processes image into an array of vectors
    and decodes the vectors to make object classification predictions
    '''
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    model = ResNet50(weights='imagenet')
    features = model.predict(x)
    results = decode_predictions(features, top=3)[0]
    preds = {tup[1]: tup[2] for tup in results}
    return preds

# url = 'https://wordpress.accuweather.com/wp-content/uploads/2018/05/forest-1.jpg'
# print(resnet_model(process_img_path(url)))
