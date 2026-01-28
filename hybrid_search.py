def vector_search(query):
    return ["Vector result 1", "Vector result 2"]

def bm25_search(query):
    return ["BM25 result A", "BM25 result B"]

def hybrid_search(query):
    return vector_search(query) + bm25_search(query)
