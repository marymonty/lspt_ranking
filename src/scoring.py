from .local_weights import get_weights
from .defines import RELEVANCY, CENTRALITY

def make_scores(docs_relevancy: {any : float}, 
                docs_centrality: {any : float}) \
                -> {any : str}:
    
    weights = get_weights()
    scores = {}
    for docid in docs_relevancy.keys():
        scores[docid] = docs_relevancy[docid]*weights.get(RELEVANCY) + \
                        docs_centrality[docid]*weights.get(CENTRALITY)
    return scores