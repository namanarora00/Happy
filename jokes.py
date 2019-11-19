import requests
import json

URL = "http://api.icndb.com/jokes/random?exclude=[explicit]"


def get_random_joke():
    res = requests.get(URL)
    res = json.loads(res.text)

    return res['value']['joke']


if __name__ == '__main__':
    print(get_random_joke())
