from .init_docs import get_prelim_docs_and_scores

def GET(words: str, n_results: int) -> {any : str}:
    docs = get_prelim_docs_and_scores(words)