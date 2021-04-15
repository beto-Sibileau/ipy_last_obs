
import requests

def api_request(address, params=None, headers=None):
    response = requests.get(address, params=params, headers=headers)
    return response