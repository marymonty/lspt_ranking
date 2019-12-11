"""Contains functionality related to the final ranking scores returned.

Weighted compilation of all gathered scores and filtering of top N results.

Typical usage example:
    If 
"""
from .local_weights import get_weights
from .defines import RELEVANCY, CENTRALITY

def make_scores(docs_relevancy: {any : float}, 
                docs_centrality: {any : float},
                n_results: int) \
                -> {any : str}:
    """Computes a weighted sum of all scores compiled.
    Args:
        docs_relevancy: A dictionary of doc IDs mapped to their relevancy
                        scores.
        docs_centrality: A dictionary of doc IDs mapped to their centrality
                         scores.
        n_results: The number of results to be returned.
    Returns:
        A dictionary containing n_results of document IDs mapped to a float
        of their final ranking score.
    """
    weights = get_weights()
    scores = {}
    for docid in docs_relevancy.keys():
        scores[docid] = str(docs_relevancy[docid]*weights.get(RELEVANCY) + \
                        docs_centrality[docid]*weights.get(CENTRALITY))
    scores = filter_scores(scores, n_results)
    return scores

def filter_scores(scores: {any : float}, n_results: int):
    """Filters the document IDs not in the top N ranked scores.
    Args:
        scores: A dictionary of document IDs mapped to their final ranking
        score.
        n_results: The number of results to be returned.
    Returns:
        Does not return anything.
    """
    score_items = [(k,v) for k,v in scores.items()]
    score_items.sort(key=lambda x: x[1], reverse=True)
    score_items = score_items[:n_results]
    return dict(score_items)