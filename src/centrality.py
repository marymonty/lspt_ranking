"""Implementation of Link Analysis communication.
Module description:
	Takes our document dictionary, docs, and sends it to Link analysis
	as a json string and receives back from Link analysis a json that 
	includes pagerank scores accompanying each documentID. These pagerank
	scores then get scaled and put into our internal docs dict.
Typical usage example:
	We start with docs, our document dictionary which would look like this:
	{ docID1 : prelim_score as float,
	  docID2 : prelim_score as float, ...}
	we send these docs to LA to get their pagerank scores which returns:
	{ docID1 : pagerank score as float,
	  docID2 : pagerank score as float, ...}
	which we then incorporate into the scores in docs.
"""
import json

from .outgoing_server import make_get_request
from .defines import LINKAN


def get_centrality(docs: [any]) -> {any : float}:
    """Gets the document scores from link analysis.
	Calls the link analysis endpoint with our document dictionary.
	Then calls _scale_la_scores to get the scaled scores based on the 
	scores given by link analysis.
	Args:
		LINKAN: the define of the link analysis endpoint.
		json.dumps(docs): the creation of a json string of our document dictionary.
	Returns:
		la_res: the link analysis response with our internal scaling on it.
	"""
    la_res = make_get_request(LINKAN, json.dumps(docs))
    _scale_la_scores(la_res)
    return la_res

def _scale_la_scores(docs: {any : float}):
    """Scales the given link analysis document scores.
	Takes the given link analysis scores and scales them and inputs them into 
	our document dictionary, docs. This function does not have a return, but it 
	does update docs.
	Args: 
		docs: our document dictionary that holds the docIDs and their scores.
	Returns: 
		none
	"""
    mx_val = max(x for x in docs.values())
    for doc in docs.keys():
        docs[doc]/=mx_val
