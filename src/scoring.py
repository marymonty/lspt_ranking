from .local_weights import get_weights
from .defines import RELEVANCY, CENTRALITY

def make_scores(docs_relevancy: {any : float}, 
                docs_centrality: {any : float},
                n_results: int) \
                -> {any : str}:
    
    weights = get_weights()
    scores = {}
    for docid in docs_relevancy.keys():
        scores[docid] = str(docs_relevancy[docid]*weights.get(RELEVANCY) + \
                        docs_centrality[docid]*weights.get(CENTRALITY))
    scores = filter_scores(scores, n_results)
    return scores

def filter_scores(scores, n_results: int):
    """
    takes the top n scores
    """
    score_items = [(k,v) for k,v in scores.items()]
    score_items.sort(key=lambda x: x[1], reverse=True)
    # print("HELLO", score_items)
    score_items = score_items[:n_results]
    return dict(score_items)