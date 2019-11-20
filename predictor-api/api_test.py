import requests
import json

if __name__ == '__main__':
    url = "https://pic-metric1.herokuapp.com/predictor"
    # url = 'http://127.0.0.1:5000/predictor' # if you want to test local
    # url = "my-heroku-app.heroku.com" # if you want to test deployed

    # this assumes that the agreed upon json key is `key`
    # WORKS
    # photo_url = 'https://upload.wikimedia.org/wikipedia/en/e/e9/Gandalf600ppx.jpg'
    # WORKS
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/c/cb/Pineapple_and_cross_section.jpg'
    photo_url = 'https://upload.wikimedia.org/wikipedia/commons/b/ba/Ribot_Theodule_The_Cook_And_The_Cat-1.jpg'
    # 'key' is used within a route like a dictionary key
    val = {'url': photo_url, 'photo_id': 1234567}
    r_success = requests.post(url, data=json.dumps(val))

    print(f'request responded: {r_success}.')
    if r_success.status_code == 200:
        print(f'the content of the response was {r_success.json()}')
    # you'll get a 200 response if the keys align,
    # and something bad if the keys don't align.
