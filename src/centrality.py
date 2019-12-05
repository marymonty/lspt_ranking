import json

from .outgoing_server import make_get_request
from .defines import LINKAN


def get_centrality(docs: [any]) -> {any : float}:
    la_res = make_get_request(LINKAN, json.dumps(docs))
    _scale_la_scores(la_res)
    return la_res

def _scale_la_scores(docs: {any : float}):
    mx_val = max(x for x in docs.values())
    for doc in docs.keys():
        docs[doc]/=mx_val