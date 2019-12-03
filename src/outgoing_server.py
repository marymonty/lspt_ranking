"""Contains functionality for communicating with external teams.
"""
import requests
import json
from .defines import ENDPOINT_PATH
from .errors import EndpointException

def _make_get_request(endpoint: str, params: {}) -> {}:
    """Makes a GET request to the endpoint specified with the params passed in.

    Ensures that the endpoint to be called is detailed as trusted and known on the
    server's endpoint.json file. Makes a GET request to the corresponding endpoint
    specified, with the params, and returns the corresponding response to the function
    caller.

    Args:
        endpoint: Endpoint's name.
        params: The outgoing GET request's parameters.

    Raises:
        EndpointException: When the endpoint called is not known; it does not exist
        in the endpoints.json file on the server.

    Returns:
        The GET request's corresponding response.
    """
    with open(ENDPOINT_PATH, 'r') as f:
        endpoints = json.load(f)
    
    if endpoint not in endpoints:
        raise EndpointException("Endpoint called does not exist.")

    res = requests.get(url = endpoints.get(url = 'url', params = params))

    return res