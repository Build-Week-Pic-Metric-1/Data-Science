<<<<<<< HEAD:classifier/predict.py
# imports
from flask import Flask, request

app = Flask(__name__)
 
@app.route('/predictor', methods=['POST'])
def predictor():
    '''a route that expects an image url and id. returns image classifications, probabilities, and id'''

    
    # get info from backend 
    lines = request.get_json(force=True)
    
    # get strings from json
    url = lines['url'] # json key that backend specifies
    photo_id = lines['photo_id'] 

    # make sure the input's correct
    assert isinstance(url, str)
    assert isinstance(photo_id, int)

    # TODO: Kyle and Oscar write the actual model here
    
    # predict
    output = model.predict([url]) # something like this?
    # ouput = ['bird', 'plane', 'superman']

    
    # format output for json
    send_back = {
        'classification_1': output[0],
        'classification_2': output[1],
        'classification_3': output[2]
        }
    
    # send output to backend
    return app.response_class(
        response=json.dumps(send_back),
        status=200
    )


if __name__ == '__main__':
    app.run()
=======
# imports
from flask import Flask, request

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    '''a route that expects an image url and id. returns image classifications,
    probabilities, and id'''

    # get info from backend
    lines = request.get_json(force=True)

    # get strings from json
    url = lines['url']  # json key that backend specifies
    photo_id = lines['photo_id']

    # make sure the input's correct
    assert isinstance(url, str)
    assert isinstance(image_id, str)

    # TODO: Kyle and Oscar write the actual model here

    # predict
    output = model.predict([url])  # something like this?

    # format output for json
    send_back = {
        'classification_1': output[0],
        'classification_2': output[1],
        'classification_3': output[2]
        }

    # send output to backend
    return app.response_class(
        response=json.dumps(send_back),
        status=200
    )


if __name__ == '__main__':
    app.run()
>>>>>>> b2857251a5abdaf3fb450f15dd967c1f9e5e3fe3:predict.py
