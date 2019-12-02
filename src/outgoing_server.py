import requests
import json
from .defines import ENDPOINT_PATH
from .errors import EndpointException

def make_get_request(endpoint: str, params: {}) -> {}:
    '''
    param endpoint: name of endpoint
    param params: whatever the parameters of the get request are

    throws: EndpointException. When the endpoint called is not inthe endpoints.json file

    returns: whatever the request returned

    '''
    with open(ENDPOINT_PATH, 'r') as f:
        endpoints = json.load(f)
    
    if endpoint not in endpoints:
        raise EndpointException("Endpoint called does not exist")

    res = requests.get(url = endpoints.get(url = 'url', params = params))

    return res