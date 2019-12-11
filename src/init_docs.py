"""Implementation of Text Transformation and Indexing communication.

In this file, we call the Text Transformation and Indexing endpoints. 
We then create a dictionary of document id's and their preliminary scores
made from the TT n_grams and Indexing occurrance scores.

Typical usage example:
    If the query is "where in new york is rpi", the resulting n-grams would be:
        unigrams: [where, new, york, rpi],
        bigrams: [where new, new york, york rpi],
        trigrams: [where new york, new york rpi],
        4-grams: [where new york rpi])
    When sent to indexing, they would return a json string formatted as follows:
        { docID1 : [tf: float, idf: float, tf-idf: float],
          docID2 : [tf: float, idf: float, tf-idf: float] ... }
    Our final document dictionary will look like this:
        { docID1 : prelim_score as float,
          docID2 : prelim_score as float, ...}
"""
from .outgoing_server import make_get_request
from .defines import INDEXING, TT

def get_prelim_docs_and_scores(words: str) -> {any : float}:
    """Retrieves the document IDs corresponding to the query words.
    1. Calls Text Transformation to extract all n-grams (n = 1, 2, 3, ....) from the query.
    2. Send all resulting n-grams to Indexing through exact match. In turn, Indexing returns the
    document IDs with their corresponding occurrence scores.
    Args:
        words: The query, represented as a string.
    Returns:
        A JSON string list of document IDs, with their respective TF, IDF, and TF-IDF scores,
        as floats.
        The overall resulting form is like so:
            { docID1 : [tf: float, idf: float, tf-idf: float],
              docID2 : [tf: float, idf: float, tf-idf: float] }
    """
    tt_req = _make_tt_req(words)
    tt_res = make_get_request(TT, tt_req)
    idx_req = _make_idx_req(tt_res)
    idx_res = make_get_request(INDEXING, idx_req)
    docs = _get_docs_and_scores(idx_res)
    return docs

def _make_tt_req(words: str):
    """Creates the formatted Text Transformation request JSON.
    Following the Text Transformation API, create the properly formatted
    json string that will be sent to the TT endpoint for them to extract 
    x number of n-grams from. This request gets returned to the 
    get_prelim_docs_and_scores function.
    Args:
        words: the query, represented as a string.
    Returns:
        A JSON string of what format we are requesting from Text
        Transformation (TT).
    """
    req = {
        "type" : "text",
        "data" : words,
        "tranformations" : {
            "stripped" : True,
            "grams" : [x for x in range(len(words.split()))]
        },
        "title" : False
    }
    return req

def _make_idx_req(tt_res):
    """Collecting the n-grams from the Text Transformation response.
    Goes through the Text Transformation response to find all the n_grams 
    then appends it to a list of n_grams, which gets returned to 
    get_prelim_docs_and_scores.
    Args:
        tt_res: the text transformation response, a JSON string.
    Returns:
        A list of n_grams from the TT service response.
    """
    n_grams = []
    for _, grams_occ in tt_res.get("grams").items():
        for gram in grams_occ.keys():
            n_grams.append(gram)
    return n_grams

def _get_docs_and_scores(idx_res):
    """Creating the dictionary of documents and their occurrance scores.
    Go through the index response to find all the document data to create the
    keys in the docs dictionary.
    _add_prelim_scores will be called to add the values.
    Args:
        idx_res: the response from indexing of a JSON with documents and
        occurrance scores.
    Returns:
        A dictionary of documents IDs mapped to their initial scores.
    """
    docs = {}
    for n_gram, docdata in idx_res.items():
        for docid in docdata.keys():
            docs[docid] = 0
    _add_prelim_scores(docs, idx_res)
    return docs

def _add_prelim_scores(docs: {any, float}, idx_res):
    """Adds the scores as values in the document id dictionary.
    Goes through the index response JSON to pull out the tf-idf scores given to each
    document to fill the values of our docs dictionary. This function changes the docs
    dictionary, without returning anything.
    Args:
        docs: A document dictionary with document ID keys mapped to their
        prelim scores as a float as the value.
        idx_res: Indexing's JSON response of doc IDs and their respective
        occurrance scores.
    Returns:
        Does not return anything.
    """
    mx_val = 0
    for n_gram, docdata in idx_res.items():
        for docid, tf_idf in docdata.items():
            docs[docid] += tf_idf.get('tf-idf')
            mx_val = max(docs[docid], mx_val)
    for doc in docs.keys():
        docs[doc]/=mx_val
