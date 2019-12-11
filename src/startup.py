"""Initializes and performs necessary startup operations for the Ranking team's server.

Typical usage example:
    # Initialize the service.
    startup()
"""
import os
import json
import sys
from shutil import copyfile

from .defines import RELEVANCY, CENTRALITY, ENDPOINT_PATH, WEIGHT_PATH

def startup():
    """Initializes the server, paths within the server, and stable storage.
    """
    create_storage()
    add_server_paths()

def create_storage():
    """Creates the directory, file, and default values for the weights.

    Makes the /bin directory if it does not exist on the server, then creates
    or opens the file used to store the weights. A JSON string composed of the
    weights is written to this file.
    """
    if not os.path.exists('lspt_ranking/bin'):
        os.mkdir('lspt_ranking/bin')
    if not os.path.exists('lspt_ranking/bin/weight_file.json'):
        with open(WEIGHT_PATH, mode='w+') as file:
            def_weights = {RELEVANCY: 0.5, CENTRALITY: 0.5}
            file.write(json.dumps(def_weights))

def add_server_paths():
    """Retrieves and populates the ENDPOINT_PATH constant.

    Makes the /bin directory if it does not exist on the server. If the endpoints.json
    file is missing on the server, an error is printed to STDERR. Otherwise, the
    ENDPOINT_PATH constant from the defines module is populated by the contents of
    the endpoints.json file.
    """
    if not os.path.exists('lspt_ranking/bin'):
        os.mkdir('lspt_ranking/bin')
    if not os.path.exists('lspt_ranking/endpoints.json'):
        print("WARNING: lspt_ranking/endpoints.json must exist", file=sys.stderr)
    else:
        copyfile('lspt_ranking/endpoints.json', ENDPOINT_PATH)
