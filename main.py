import time

from asr_stream import stream_asr
from query_rewriter import rewrite_query
from hybrid_search import hybrid_search
from reranker import rerank
from llm_stream import llm_stream
from tts_stream import stream_tts

# ----------------------------
# Utility for timestamped logs
# ----------------------------
START_TIME = time.time()

def log(message):
    elapsed = round(time.time() - START_TIME, 3)
    print(f"[{elapsed}s] {message}")

# ----------------------------
# Conversation state
# ----------------------------
chat_history = ["router reset steps"]

log("Voice RAG system started")

# ----------------------------
# Simulated streaming ASR loop
# ----------------------------
for partial_text in stream_asr(None):

    log(f"ASR partial received: '{partial_text}'")

    # ---- Query Rewriting (handles references like 'second one')
    rewritten_query = rewrite_query(partial_text, chat_history)
    log(f"Rewritten query: '{rewritten_query}'")

    # ---- Start RAG pre-fetch immediately (parallel intent)
    rag_results = hybrid_search(rewritten_query)
    log("Hybrid search triggered (Vector + BM25)")

    # ---- Start LLM + TTS immediately (latency masking)
    log("Starting LLM filler + streaming TTS (masking latency)")
    llm_output_stream = llm_stream(rewritten_query)
    stream_tts(llm_output_stream)

    # ---- Reranker runs in parallel (simulated slow operation)
    log("Cross-encoder reranker running...")
    top_context = rerank(rag_results, rewritten_query)
    log(f"Reranking complete. Top context: {top_context}")

    # ---- Update conversation memory
    chat_history.append(rewritten_query)

log("Voice RAG session ended")
