import requests
import json

if __name__ == '__main__':
    # url = "https://pic-metric1.herokuapp.com/predictor"  # if you want to test local
    url = 'http://127.0.0.1:5000/predictor'
    # url = "my-heroku-app.heroku.com" # if you want to test deployed

    # this assumes that the agreed upon json key is `key`
    # WORKS
    # photo_url = 'https://upload.wikimedia.org/wikipedia/en/e/e9/Gandalf600ppx.jpg'
    # SOMETIMES WORKS / SOMETIMES DOES NOT WORK
    # photo_url = 'https://miro.medium.com/max/15904/1*eG2MFl0sGRKFmd_USgA_8Q.jpeg'
    # SOMETIMES WORKS / SOMETIMES DOES NOT WORK
    # photo_url = 'http://www.sabretravelnetwork.com/images/uploads/hero-developers.jpg' 
    # WORKS AND DOESN'T WORK
    # photo_url = 'https://www.computerhope.com/jargon/d/developer.jpg'
    # photo_url = 'https://wordpress.accuweather.com/wp-content/uploads/2018/05/forest-1.jpg'
    photo_url = 'https://www.aithority.com/wp-content/uploads/2019/06/Terminator-Teaches-Us-About-AI-and-the-Need-for-Better-Data-guest-post-770x410.jpg'
    # 'key' is used within a route like a dictionary key
    val = {'url': photo_url, 'photo_id': 1234}
    r_success = requests.post(url, data=json.dumps(val))

    print(f'request responded: {r_success}.')
    if r_success.status_code == 200:
        print(f'the content of the response was {r_success.json()}')
    # you'll get a 200 response if the keys align,
    # and something bad if the keys don't align.
