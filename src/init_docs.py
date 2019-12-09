from .outgoing_server import make_get_request
from .defines import INDEXING, TT

def get_prelim_docs_and_scores(words: str) -> {any : float}:
    tt_req = _make_tt_req(words)
    tt_res = make_get_request(TT, tt_req)
    idx_req = _make_idx_req(tt_res)
    idx_res = make_get_request(INDEXING, idx_req)
    docs = _get_docs_and_scores(idx_res)
    return docs

def _make_tt_req(words: str):
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
    n_grams = []
    for _, grams_occ in tt_res.get("grams").items():
        for gram in grams_occ.keys():
            n_grams.append(gram)
    return n_grams

def _get_docs_and_scores(idx_res):
    docs = {}
    for n_gram, docdata in idx_res.items():
        for docid in docdata.keys():
            docs[docid] = 0
    _add_prelim_scores(docs, idx_res)
    return docs

def _add_prelim_scores(docs: {any, float}, idx_res):
    mx_val = 0
    for n_gram, docdata in idx_res.items():
        for docid, tf_idf in docdata.items():
            docs[docid] += tf_idf.get('tf-idf')
            mx_val = max(docs[docid], mx_val)
    for doc in docs.keys():
        docs[doc]/=mx_val