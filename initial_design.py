import json





def POST(words: [str], 
          weights: { popularity: [float], recency: [float], exact: [bool] },
          results: [int] )  -> {any : float}:
    """Post guides a request through the ranking process.

    Querying will call this POST with the user query. This function will take the words (query), 
    weights (three groups of weights: popularity, recency, expressed as strings representing floats, floats, and bools),
    and results (a string representing an int of the number of results querying wants) and will make internal calls 
    to pass this information to other functions to eventually rank and return.

    Args:
        -words: the query, represented as a string
        -weights: -popularity: the popularity metric the user wants weighted by, a float represented as a string in json
                  -recency: the recency metric the user wants weighted by, a float represented as a string in json
                  -exact: the exact metric if the user wants exact match, a boolean true or false represented as a json string
        -results: an integer of how many results UI wants to display

    Returns:
        -ranked_list: a list of documents and their scores (compiled via their occurance score, link score, and metadata) in a json string 
    """
    pass



#(we will make all of these comments formatted correctly, but we have not gotten to do it yet so here are simple descriptions)



def Get_Prelim_Documents(words: [any]) -> {any : { tf: [int], idf: [int], tf-idf: [int] }}:
    """Get_Prelim_Documents will use the query to get initial scores on the query.

    This function will call text transformation first to get all possible n-grams from the query (1-grams, 2-grams, 3-grams etc) 
    (for example: if query is "where in new york is rpi" we would get 1-grams [where, new, york, rpi], 2-grams [where new, new york, york rpi],
    3-grams [where new york, new york rpi], and 4-grams [where new york rpi]). The function will then take all of these n-grams and send them
    to indexing through their exact match function. Indexing will return to us the document ids with their occurrence scores in the form of 
    { doc : [tf: int as string, idf: int as string, tf-idf: int as string] }

    Params:
        -words: the query, represented as a string

    Returns:
        -occ_scores- the json string list of document ids, with their accompanying tf, idf, and tf-idf scores as int written as strings
            in the form { docID1 : [tf: int as string, idf: int as string, tf-idf: int as string],
                          docID2 : [tf: int as string, idf: int as string, tf-idf: int as string] }
    """
    pass

def Get_Link_Analysis(docids: [any]) -> {any : float}:
    """Get_Link_Analysis will be a function to interact with Link Analysis.

    This function will call link analysis to get their pagerank ranked list of docIDs. We will send them a list of docIDS as a json object
    and they will rank them based on their internal graph and will return to us a list of docIDS with their accompanying pagerank scores
    in the form { url1: { pagerank: float as string },
                  url2: { pagerank: float as string } } 

    Params:
        -docids: the list of document ids (gotten from indexing)

    Returns:
        -link_scores: the json string of the list of urls and their pagerank scores in the format:
            { url1: { pagerank: int as string },
              url2: { pagerank: int as string } }
            if any of the links are not in the link_analysis graph they return a score of 0 for pagerank
    """
    pass

def Get_Metadata_Score(docids: [any]) -> {any : float}:
    """Get_Metadata_Score is a function to get any needed metadata information from DDS.

    This function will be called if we need any other metadata from Document Data Stroage that we may need to rank.
    We use DDS to call a GET command. Metadata will return to us the response GET command which will either contain 
    an error message or the document and all information that DDS has on the document (url, id, title, body, words, 
    bigrams, trigrams, crawledDateTime, recrawlDateTime, anchors)

    Params:
        -docids: the json string of a list of document ids

    Returns:
        -meta_scores: any of the useful data gotten from the DDS GET response
    """
    pass

def Compile_Scores(occ_scores: {any : float}, 
                    link_scores: {any : float}, 
                    meta_scores: {any : float}) -> {any : float}: 
    """Compile_Scores is our internal ranking function.

    This function will take the occrrence scores from indexing, the pagerank scores from link analysis, and the 
    metadata scores from document data storage. We will compile these scores by ???????????????. The result will
    be a json list of the document ids with their normalized scores as floats between 0 and 1.

    Params:
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

def Get_Weights() -> {str : float}:
    """
    Get a list of weights and their values to use in the ranking process.

    This function will return the weights that are given to each category of measurement, and return them to use 
	in compile scores.

	Params:
		None

	Returns:
		-the JSON Dictionary Weights of each category.

   
    """
    pass
