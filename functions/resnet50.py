import numpy as np

from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

def process_img_path(img_path):
  ''' Processes image url and compresses it to 224 x 224 pixels'''
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