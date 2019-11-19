import numpy as np

from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

from PIL import Image
import requests
from io import BytesIO


url = 'https://en.wikipedia.org/wiki/Gandalf#/media/File:Gandalf600ppx.jpg'

def process_img_path_url(img_path):
    ''' Process image url and compresses it to 224 x 224'''
    response = requests.get(img_path)
    img = Image.open(BytesIO(response.content))
    return img

def process_img_path_local(img_path):
  ''' Processes local image path and compresses it to 224 x 224 pixels'''
  return image.load_img(img_path, target_size=(224, 224))

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
    preds = {tup[1]:tup[2] for tup in results}
    return preds

print(resnet_model(process_img_path(url)))