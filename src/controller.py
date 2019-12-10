"""Our API call, takes in the query and creates the ranked results dict.
Module description:
	This module covers our GET request, where we are called with a query
	and an int of how many results are wanted. We take this query and call
	other modules that call Text Transformation, Indexing, and Link Analysis
	in order to compile all the scores associated with a result link. These
	scores get internally compiled and calculated to give a final score for 
	a result link.
Typical usage example:
	We receive a query, "where in new york is rpi" and the int 300, which
	means querying wants 300 results. We send this query to other modules which
	return docs, the updated dictionary of document ids and their associated
	scores. We end with the final docs list with their accompanying ranked scores.
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
		words: the initial query string.
		n_results: int of how many results should be returned.
	Returns:
		scored_docs: the final version of our docs dictionary of docIDs
		and their accompanying final ranked score, a float between 0 and 1.
	"""
    docs_relevancy = get_prelim_docs_and_scores(words)
    docs = list(docs_relevancy.keys())

    docs_centrality = get_centrality(docs)
    scored_docs = make_scores(docs_relevancy, docs_centrality, n_results)
    return scored_docs
    
