# Zero-Latency Voice RAG System

## Overview
This project demonstrates a **zero-latency, voice-first Retrieval Augmented Generation (RAG) pipeline**
designed for CCaaS platforms. The system assists users in troubleshooting complex hardware issues by
querying large technical manuals (1,000+ pages) and responding via voice.

The primary objective is to achieve **sub-800ms Time-to-First-Byte (TTFB)** for audio responses, even
when handling complex multi-document queries.

---

## Architecture Highlights

### 1. Parallelized (Speculative) RAG Pipeline
Traditional voice pipelines follow a linear flow:
ASR → RAG → LLM → TTS

This approach introduces high latency.  
Instead, this system uses **speculative execution**:

- Streaming ASR produces partial transcripts
- RAG pre-fetch begins as soon as partial ASR output is available
- LLM generation and TTS streaming start before retrieval fully completes

This significantly reduces perceived latency and improves responsiveness.

---

### 2. Query Rewriting (Conversational Context Resolution)
The system handles conversational follow-up queries such as:
> “And what about the second one?”

Before querying the vector database, ambiguous references are resolved using
conversation history.

Example rewritten query:


This ensures accurate retrieval and demonstrates context-aware reasoning.

---

### 3. Hybrid Search with Reranking
To improve retrieval quality for technical queries, the system uses:

- **Vector Search** for semantic similarity
- **BM25** for keyword-based matching
- **Cross-Encoder Reranker** for final relevance scoring

Since rerankers introduce additional latency, their cost is masked by
streaming a **filler voice response** (e.g., *“Let me check the technical manual for that…”*)
while reranking completes in parallel.

---

### 4. Voice-Optimized Output
LLM outputs are post-processed into **spoken English** to improve voice delivery:

- Short, simple sentences
- Voice-friendly phrasing
- Chunked output for faster TTS synthesis

This avoids robotic speech and improves the end-user experience.

---

## Latency Strategy

| Pipeline Stage | Optimization |
|---------------|--------------|
| ASR | Streaming partial transcripts |
| Retrieval | Speculative RAG pre-fetch |
| Reranking | Parallel execution |
| LLM | Streaming token generation |
| TTS | Chunked audio output |

Audio streaming begins **before reranking completes**, enabling sub-800ms
perceived audio TTFB.

---

## Tech Stack
- Python 3.10
- Simulated Streaming ASR
- Hybrid Retrieval (Vector + BM25)
- Cross-Encoder Reranker (simulated)
- Streaming LLM Output
- Voice-Optimized Post-Processing

---

## How to Run

```bash
py -3.10 main.py

