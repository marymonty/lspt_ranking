"""Contains functionality for retrieving and setting the weight values stored locally.
"""

import os
import json
from .defines import WEIGHT_PATH, RELEVANCY, CENTRALITY
from .errors import WeightNotExist

def get_weights() -> {}:
    """Retrieves the weights to be used from stable storage.

    Raises:
            WeightNotExist: If weights file does not exist.

    Returns:
        A dictionary with the float weight values.
    """
    if not os.path.exists(WEIGHT_PATH):
        raise WeightNotExist('Weights file does not exist.')

    with open(WEIGHT_PATH, 'r') as file:
        weights = json.load(file)
        return weights

def _set_weights(relevancy: float, centrality: float) -> bool:
    """Sets weights on local storage as specified.

    Ensures that the weights passed in sum to 1.0. If they do, converts them to a JSON string,
    and populates the stable storage file specified in the WEIGHT_PATH constant. The weights
    used to populate the file are returned to the function caller.

    Args:
        popularity: A float representative of how much the popularity metric is weighted.
        recency: A float representative of how much the float metric is weighted.
        relevancy: A float representative of how much the relevancy metric is weighted.

    Returns:
        If the weights specified do not sum up to 1.0 (i.e. are not normalized), a False
        boolean is returned to the function caller. It is up to the function caller to
        check if a False has been returned.
        Otherwise, the weights are updated in file, and are returned to the user in
        dictionary form.
    """
    if centrality + relevancy != 1.0:
        return False
    weights = {RELEVANCY: relevancy, CENTRALITY: centrality}

    with open(WEIGHT_PATH, 'w') as file:
        weights = json.load(file)
        return weights

    return True
