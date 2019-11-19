if __name__=='__main__':
    url = "localhost:5000" # if you want to test local
    # url = "my-heroku-app.heroku.com" # if you want to test deployed 
    
    # this assumes that the agreed upon json key is `key` 
    val = {'url': 'https://photo.com/', 'photo_id': 1234} # 'key' is used within a route like a dictionary key
    r_success = requests.post(url, data=json.dumps(val))
    
    print(f"request responded: {r_success}.\nthe content of the response was {r_success.json()}")
    # you'll get a 200 response if the keys align, and something bad if the keys don't align. 