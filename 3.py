import requests
import json


def main():
    url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token=24.89cd78d4154e278bdf50227ea7eec626.2592000.1713198852.282335-56825030&charset="

    payload = json.dumps({"text":"不错"})
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    main()
