import os
import json

from .defines import POPULARITY, RECENCY, RELEVANCY

def startup():
    create_storage()

def create_storage():
    if not os.path.exists('lspt_ranking/bin'):
        os.mkdir('lspt_ranking/bin')
    if not os.path.exists('lspt_ranking/bin/weight_file.json'):
        with open("lspt_ranking/bin/weight_file.json", mode="w+") as f:
            def_weights = {POPULARITY: 0.34, RECENCY: 0.33, RELEVANCY: 0.33}
            f.write(json.dumps(def_weights))
