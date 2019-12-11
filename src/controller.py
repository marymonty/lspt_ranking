"""Ranking's API call, takes in a query, and creates the ranked results
dictionary.

This module covers the GET request. It guides the request through other
modules that call the Text Transformation, Indexing, and Link Analysis
teams in order to compile scores from each team. These scores are internally
compiled and calculated to give a final score for each result link.

Typical usage example:
    We receive a query, "where in new york is rpi" and the int 300, which
    means the function caller wants 300 results. We send this query to other
    modules which return docs, the updated dictionary of document ids and their
    associated scores. We end with the final docs list with their
    accompanying ranked scores.
"""
from .init_docs import get_prelim_docs_and_scores
from .centrality import get_centrality
from .scoring import  make_scores

def GET(words: str, n_results: int) -> {any : str}:
    """Takes the query and returns the ranked resulting pages.
    Takes in the inital string query and the amount of results to know how many
    results to return. This function calls our other files that contain functions
    to get the scores from indexing and link analysis. It also calls our internal 
    functions to calculate our final ranked scores, which we update in docs and return
    to the caller of this function.
    Args:
        words: The initial query.
        n_results: How many results should be returned.
    Returns:
        A dictionary of document IDs mapped to their accompanying final ranked
        score. The final ranked score will be a float between 0 and 1.
    """
    docs_relevancy = get_prelim_docs_and_scores(words)
    docs = list(docs_relevancy.keys())

    docs_centrality = get_centrality(docs)
    scored_docs = make_scores(docs_relevancy, docs_centrality, n_results)
    return scored_docs
    
