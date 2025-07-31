# 📊 Retrieval 평가

Query-Document 검색 평가\
Test case 80\
Number of Documents 500

## 🧭 전체 평가 흐름 (Evaluation Flow)
```
[1] Query regeneration
[2] search
```


<br>

### 📌 [1] Query regeneration
- 목적: Query에 따라 달라지는 점수 비교
- 방법:
    - User Query(Baseline)
    - Keywords extraction
    - convert to Document format
- 평가 지표:
    - Recall

### 📌 [2] search
- 목적: Search Algorithm에 따라 달라지는 점수 비교
- 방법:
    - BM25
    - Hybrid
    - LLM Reranker
- 평가 지표:
    - Recall