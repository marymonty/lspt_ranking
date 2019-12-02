import os
import json
import sys
from shutil import copyfile

from .defines import POPULARITY, RECENCY, RELEVANCY, ENDPOINT_PATH, WEIGHT_PATH

def startup():
    create_storage()
    add_server_paths()

def create_storage():
    if not os.path.exists('lspt_ranking/bin'):
        os.mkdir('lspt_ranking/bin')
    if not os.path.exists('lspt_ranking/bin/weight_file.json'):
        with open(WEIGHT_PATH, mode="w+") as f:
            def_weights = {POPULARITY: 0.34, RECENCY: 0.33, RELEVANCY: 0.33}
            f.write(json.dumps(def_weights))

def add_server_paths():
    if not os.path.exists('lspt_ranking/bin'):
        os.mkdir('lspt_ranking/bin')
    if not os.path.exists('lspt_ranking/endpoints.json'):
        print("WARNING: lspt_ranking/endpoints.json must exist", file=sys.stderr)
    else:
        copyfile('lspt_ranking/endpoints.json', ENDPOINT_PATH) 