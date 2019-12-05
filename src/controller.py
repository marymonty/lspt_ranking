from .init_docs import get_prelim_docs_and_scores
from .centrality import get_centrality
from .scoring import  make_scores

def GET(words: str, n_results: int) -> {any : str}:
    docs_relevancy = get_prelim_docs_and_scores(words)
    docs = docs_relevancy.keys()

    docs_centrality = get_centrality(docs)
    scored_docs = make_scores(docs_relevancy, docs_centrality, n_results)
    return scored_docs
    