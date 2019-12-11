"""Implementation of communication with the Link Analysis team.

Our dictionary of doc IDs is sent to the Link Analysis team
as a JSON string. In return, Link analysis returns a JSON of each docIDs
PageRank score. These PageRank scores are scaled and put into our internal
docs dict.

    Typical usage example:
    We start with docs, our document dictionary, which would look like this:
    { docID1 : prelim_score as float,
      docID2 : prelim_score as float, ...}
    we send these docs to LA to get their PageRank scores which returns:
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
    docs: A list of document IDs.
  Returns:
    A dictionary of the document IDs mapped to their corresponding PageRank
    score.
  """
    la_res = make_get_request(LINKAN, json.dumps(docs))
    _scale_la_scores(la_res)
    return la_res

def _scale_la_scores(docs: {any : float}):
    """Scales the given link analysis document scores.
  Scales the PageRank scores returned by the Link Analysis team. Then inputs
  them into our dictionary of document IDs. This function does not have a
  return, but it does update an internal variable, docs.
  Args:
    docs: A dictionary holding the docIDs and their PageRank scores.
  Returns:
    Does not return anything.
  """
    mx_val = max(x for x in docs.values())
    for doc in docs.keys():
        docs[doc]/=mx_val
