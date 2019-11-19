# imports
from flask import Flask, request
import json
from resnet50 import process_img_path, resnet_model

app = Flask(__name__)
 
@app.route('/predictor', methods=['POST'])
def predictor():
    '''a route that expects an image url and id. returns image classifications, probabilities, and id'''

    
    # get info from backend 
    lines = request.get_json(force=True)
    
    # get strings from json
    url = lines['url']
    photo_id = lines['photo_id'] 

    # make sure the input's correct
    assert isinstance(url, str)
    assert isinstance(photo_id, int)

    # process image and predict
    predictions = resnet_model(process_img_path(url))

    # predict
    # predictions = resnet_model(processed_url)
    # output = ['bird', 'plane', 'superman']

    
    # format output for json
    send_back = {
        'predictions': predictions
    }
    # send_back = {
    #     'url_sent': url,
    #     'id_sent': photo_id
    # }
    # send_back = {
    #     'classification_1': output[0],
    #     'classification_2': output[1],
    #     'classification_3': output[2]
    #     }
    
    # send output to backend
    return app.response_class(
        response=json.dumps(send_back),
        status=200
    )


if __name__ == '__main__':
    app.run()