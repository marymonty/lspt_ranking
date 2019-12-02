import os
import json
from .defines import WEIGHT_PATH, POPULARITY, RELEVANCY, RECENCY
from .errors import WeightNotExist

def get_weights() -> {}:
    """Retrieves the weights to be used fro stable storage.

    Raises:
            WeightNotExist: If weights file does not exist.

    Returns:
        A dictionary with the float weight values.
    """
    if not os.path.exists(WEIGHT_PATH):
        raise WeightNotExist('Weights file does not exist.')

    with open(WEIGHT_PATH, 'r') as f:
        weights = json.load(f)
        return weights

def set_weights(popularity: float, recency: float, relevancy: float) -> bool:
    """Sets weights 
    """
    if popularity + recency + relevancy != 1.0:
        return False
    weights = {POPULARITY: popularity, RECENCY: recency, RELEVANCY: relevancy}

    with open(WEIGHT_PATH, 'w') as f:
        weights = json.load(f)
        return weights

    return True