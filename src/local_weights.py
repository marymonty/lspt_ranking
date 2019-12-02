import os
import json
from .defines import WEIGHT_PATH, POPULARITY, RELEVANCY, RECENCY
from .errors import WeightNotExist

def get_weights() -> {}:
    '''
    gets the different weights from stable storage

    throws weight not exist if they do not exist

    returns a dictionary with all the weights
    '''
    if not os.path.exists(WEIGHT_PATH):
        raise WeightNotExist('Weights file does not exist')

    with open(WEIGHT_PATH, 'r') as f:
        weights = json.load(f)
        return weights

def set_weights(popularity: float, recency: float, relevancy: float) -> bool:
    if popularity + recency + relevancy != 1:
        return False
    weights = {POPULARITY: popularity, RECENCY: recency, RELEVANCY: relevancy}

    with open(WEIGHT_PATH, 'w') as f:
        weights = json.load(f)
        return weights

    return True