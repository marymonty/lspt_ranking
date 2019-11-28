"""Implementation of ranking team functionality.

TODO: Write up overall description of the module or program, as well as contain a typical usage
example.
"""
import json
import requests  # Used to make HTTP requests in Python.

# Internal global variable for weight storage.
_weights = {}

def _get_weights() -> {str : float}:
    """Returns the weight values to use in the ranking process.

    This function will return the weights that are given to each category of measurement.

	Returns:
		A JSON dictionary of each category's weight.
    """
    return _weights

def _update_weights(weights: {"popularity": [float], "recency": [float], "exact": [bool]}):
    """Updates the internal global _weights variable.

    Ensures all weights sum up to 1, and sets the _weights variable accordingly.

    Args:
        weights: Floats stipulating how each metric is weighted when computing scores.
            popularity: How the popularity metric is weighted when computing overall score.
                        A float represented as a JSON string.
            recency: How the recency metric is weighted when computing overall score.
                     A float represented as a JSON string.
            exact: Stipulates if exact match is used in the ranking process.
                     A boolean represented as a JSON string.
    """
    total = 0.0
    empty_fields = 0

    _weights = weights
    for (metric, weight) in _weights:
        if weight == '':
            empty_fields += 1
        elif metric == 'exact' and weight == 'True':
            empty_fields += 1
        else:
            _weights[metric] = float(weight)  # Turn non-empty JSON string into a float.
            total += float(weight)

    if total != 1.0:
        remainder = float(total/empty_fields)
        for (metric, weight) in _weights:
            if weight == '':
                _weights[metric] = remainder

def POST(words: [str],
         weights: {"popularity": [float], "recency": [float], "exact": [bool]},
         results: [int])  -> {any : float}:
    """POST guides a request through the ranking pipeline.

    Querying will call this with the user's query, which is sent to Text Transformation. They
    return all valid n-grams, which are then passed to Indexing through exact match. Indexing
    returns relevant document IDs with their respective occurrence scores. These document IDs
    are sent to Link Analysis and Document Data Storage, which respectively return the PageRank
    scores and stored metadata for each document ID sent.

    The occurrence scores, PageRank scores, and stored metadata are compiled into an overall
    ranking score, which is returned to the initial callee.

    Args:
        words: The user query, represented as a list of strings.
        weights: Floats stipulating how each metric is weighted when computing scores.
            popularity: How the popularity metric is weighted when computing overall score.
                        A float represented as a JSON string.
            recency: How the recency metric is weighted when computing overall score.
                     A float represented as a JSON string.
            exact: Stipulates if exact match is used in the ranking process.
                     A boolean represented as a JSON string.
        results: How many results to be returned, represented as a string representing an integer.

    Returns:
        A list of documents and their respective scores as a JSON string.
        These scores are compiled via their occurrence score, link score, and metadata.
    """
    _update_weights(weights)
    doc_ids_to_occ_scores = _get_prelim_documents(words)
    doc_ids = list(doc_ids_to_occ_scores.keys())
    occ_scores = list(doc_ids_to_occ_scores.values())
    link_scores = _get_link_analysis(doc_ids)
    meta_scores = _get_metadata_score(doc_ids)

    return _compile_scores(occ_scores, link_scores, meta_scores)

def _get_prelim_documents(words: [any]) -> {any : {"tf": [int], "idf": [int], "tf-idf": [int]}}:
    """Retrieves the document IDs corresponding to the query words.

    1. Calls Text Transformation to extract all n-grams (n = 1, 2, 3, ....) from the query.
    For example:
        If the query is "where in new york is rpi", the resulting n-grams would be:
        unigrams: [where, new, york, rpi],
        bigrams: [where new, new york, york rpi],
        trigrams: [where new york, new york rpi],
        4-grams: [where new york rpi]).
    2. Send all resulting n-grams to Indexing through exact match. In turn, Indexing returns the
    document IDs with their corresponding occurrence scores like so:
    { doc : [tf: int as string, idf: int as string, tf-idf: int as string] }.

    Args:
        words: The query, represented as a string.

    Returns:
        A JSON string list of document IDs, with their respective TF, IDF, and TF-IDF scores,
        all in string form.
        The overall resulting form is like so:
            { docID1 : [tf: int as string, idf: int as string, tf-idf: int as string],
              docID2 : [tf: int as string, idf: int as string, tf-idf: int as string] }
    """
    pass

def _get_link_analysis(doc_ids: [any]) -> {any : float}:
    """Retrieves document IDs' PageRank scores from Link Analysis.

    Calls Link Analysis with a list of document IDs as a JSON object to retrieve a PageRank ranked
    list of document IDs.
    These PageRank scores are based on their internal graph representation.

    Args:
        doc_ids: A list of document ids.

    Returns:
        A JSON string of the list of document IDs, with their respecctive PageRank scores in the
        format:
            { url1: { pagerank: int as string },
            url2: { pagerank: int as string } }.
        If any of the document IDs are not in Link Analysis's internal graph, a PageRank score of
        0 is returned.
    """
    pass

def _get_metadata_score(doc_ids: [any]) -> {any : any}:
    """Retrieves metadata information pertaining to the document IDs.

    Called if additional metadata from Document Data Storage (DDS) is necessary for ranking.
    DDS is called via a GET request containing document IDs, the metadata of which is returned via
    a GET response containing either an error message, or a dictionary containing all the
    information that DDS has on the corresponding document (e.g. URL, id, title,
    body, words, bigrams, trigrams, crawledDateTime, recrawlDateTime, anchors, et cetera).

    Args:
        doc_ids: A list of document ids.

    Returns:
        A dictionary of metadata pertaining to each document ID key.
    """
    pass

def _compile_scores(occ_scores: {any : float},
                    link_scores: {any : float},
                    meta_scores: {any : float}) -> {any : float}:
    """Combines retrieved scores to form an overall ranking score.

    Compiles the occurrence, link/PageRank, and metadata scores via a weighted sum. The result will
    be a JSON list of the document ids, with their respective normalized scores as floats between
    0 and 1.

    Args:
        occ_scores: The occurrence scores received from Indexing. A JSON string formatted like so:
            { docID1 : [tf: int as string, idf: int as string, tf-idf: int as string],
              docID2 : [tf: int as string, idf: int as string, tf-idf: int as string] }).
        link_scores: The PageRank scores received from Link Analysis. A JSON string like so:
            { url1: { pagerank: int as string },
              url2: { pagerank: int as string } }).
        meta_scores: The scores of other metrics recieved from Document Data Storage.

    Returns:
        A JSON string list of document ids with their accompanying scores (between 0 and 1).
        The format would be like so:
            { docID1: { ranking: float as string },
              docID2: { ranking: float as string } }.
    """
    pass
