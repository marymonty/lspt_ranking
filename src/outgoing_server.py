"""Contains functionality for communicating with external teams.

Typical usage example:
    make_get_request(MOCKED)
"""
import json
import requests
from .defines import ENDPOINT_PATH, TT, INDEXING, DDS, LINKAN
from .errors import EndpointException, ServerErrorCode

MOCKED = False

def make_get_request(endpoint: str, data: {}) -> {}:
    """Makes a GET request to the endpoint specified with the params passed in.

    Ensures that the endpoint to be called is detailed as trusted and known on the
    server's endpoint.json file. Makes a GET request to the corresponding endpoint
    specified, with the params, and returns the corresponding response to the function
    caller.

    Args:
        endpoint: Endpoint's name.
        data: The outgoing GET request's parameters.

    Raises:
        EndpointException: When the endpoint called is not known; it does not exist
        in the endpoints.json file on the server.

    Returns:
        The GET request's corresponding response.
    """
    if MOCKED:
        return json.loads(return_mock(endpoint))

    with open(ENDPOINT_PATH, 'r') as file:
        endpoints = json.load(file)

    if endpoint not in endpoints:
        raise EndpointException("Endpoint called does not exist.")
    try:
        res = requests.post(url=endpoints.get(endpoint), json=data)
    except requests.exceptions.ConnectionError:
        raise EndpointException("Invalid endpoint %s" % endpoint, endpoint)

    if res.status_code != 200:
        raise ServerErrorCode("Call to endpoint %s \
                failed with code %d" \
                % (endpoint, res.status_code), endpoint)
    
    return json.loads(res.text)


def return_mock(endpoint: str):
    """Function used to mock other services for testing purposes.

    Args:
        endpoint: The endpoint to be mocked.
    Raises:
        EndpointException: When the endpoint called is not a predefined
        constant within the endpoints.json file on the server.
    Returns:
        An appropriate mocked response from the corresponding endpoint called.
    """
    res = ""
    if endpoint == TT:
        res = json.dumps({
	        "stripped": "hello world",
	        "grams": {
                1: {"hello": [0, 1], "world": [2]}, 
                2: {"hello hello": [0], "hello world": [1]}, 
                3: {"hello hello world": [0]}
            },
	        "title": "Hello World"
        })
    elif endpoint == LINKAN:
        res = json.dumps({
            "0" : 0.3,
            "1" : 0.3,
            "2" : 0.3
        })
    elif endpoint == INDEXING:
        res = json.dumps({
            "hello world": {"0": {"tf-idf": 0.11194170287483966}, "1": {"tf-idf": 0.38544484153148295},
	        "2": {"tf-idf": 0.12412684823499272}}
        })
    else: 
        raise EndpointException
    return res
