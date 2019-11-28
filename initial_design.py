import json
import requests  # Used to make HTTP requests in Python.

# Internal global variable for weight storage.
_weights = {}

def _update_weights(weights: {"popularity": [float], "recency": [float], "exact": [bool]}):
    """Updates the internal global _weights variable.

    Internal function. Ensures all weights sum up to 1, and sets the _weights variable accordingly.

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

    if not total == 1.0:
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
        ranked_list: A list of documents and their respective scores as a JSON string.
                     These scores are compiled via their occurrence score, link score, and metadata.
    """
    _update_weights(weights)
    pass

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
        occ_scores: A JSON string list of document IDs, with their respective TF, IDF, and
                    TF-IDF scores, all in string form.
                    The overall resulting form is like so:
                        { docID1 : [tf: int as string, idf: int as string, tf-idf: int as string],
                          docID2 : [tf: int as string, idf: int as string, tf-idf: int as string] }
    """
    pass

def _get_link_analysis(docids: [any]) -> {any : float}:
    """Get_Link_Analysis will be a function to interact with Link Analysis.

    This function will call link analysis to get their pagerank ranked list of urls. We will send them a list of
    urls as a json object and they will rank them based on their internal graph and will return to us a list of 
    urls with their accompanying pagerank scores 
    in the form { url1: { pagerank: int as string },
                  url2: { pagerank: int as string } } 

    ****************** PAGERANK IS GOING FLOAT AS A STRING**************************

    Args:
        -docids: the list of document ids (gotten from indexing)

    Returns:
        -link_scores: the json string of the list of urls and their pagerank scores in the format:
            { url1: { pagerank: int as string },
              url2: { pagerank: int as string } }
            if any of the links are not in the link_analysis graph they return a score of 0 for pagerank
    """
    pass

def _get_metadata_score(docids: [any]) -> {any : float}:
    """Get_Metadata_Score is a function to get any needed metadata information from DDS.

    This function will be called if we need any other metadata from Document Data Stroage that we may need to 
    rank. We use DDS to call a GET command. Metadata will return to us the response GET command which will either 
    contain an error message or the document and all information that DDS has on the document (url, id, title, 
    body, words, bigrams, trigrams, crawledDateTime, recrawlDateTime, anchors)

    Args:
        -docids: the json string of a list of document ids

    Returns:
        -meta_scores: any of the useful data gotten from the DDS GET response
    """
    pass

def _compile_scores(occ_scores: {any : float}, 
                    link_scores: {any : float}, 
                    meta_scores: {any : float}) -> {any : float}: 
    """Compile_Scores is our internal ranking function.

    This function will take the occrrence scores from indexing, the pagerank scores from link analysis, and the 
    metadata scores from document data storage. We will compile these scores by ???????????????. The result will
    be a json list of the document ids with their normalized scores as floats between 0 and 1.

    Args:
        -occ_scores: the occurrence scores we received from indexing (a json string of 
            { docID1 : [tf: int as string, idf: int as string, tf-idf: int as string],
              docID2 : [tf: int as string, idf: int as string, tf-idf: int as string]  })
        -link_scores: the pagerank scores we received from link analysis (a json string of 
            { url1: { pagerank: int as string },
              url2: { pagerank: int as string } })
        -meta_scores: the scores of any other metrics we recieved from document data storage

    Returns:
        -ranking_scores: the json string list of document ids with their accompanying scores (between 0 and 1)
            { docID1: { ranking: float as string },
              docID2: { ranking: float as string } }
    """
    pass

def get_weights() -> {str : float}:
    """
    Get a list of weights and their values to use in the ranking process.

    This function will return the weights that are given to each category of measurement, and return them to use 
	in compile scores.

	Returns:
		-the JSON Dictionary Weights of each category.
    """
    pass
