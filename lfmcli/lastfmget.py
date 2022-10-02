import requests
from config.request_keys_secret import API_KEY, USER_AGENT

def lastfmGet(payload):

    headers = { "user-agent": USER_AGENT }
    url = "https://ws.audioscrobbler.com/2.0/"

    payload["api_key"] = API_KEY
    payload["format"] = "json"
    
    response = requests.get(url, headers=headers, params=payload)

    return response