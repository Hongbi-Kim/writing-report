# 📊 Retrieval 평가

Query-Document 검색 평가\
Test case 80\
Number of Documents 500

## 🧭 전체 평가 흐름 (Evaluation Flow)
```
[1] Query regeneration
[2] search
```
평가 지표를 Recall로 설정한 이유: \
관련된 문서를 빠짐없이 검색하는 것이 중요하다고 판단. 관련되지 않은 문서의 경우는 2차 검색(내용 검색) 시에 걸러질 수 있음.


<br>

### 📌 [1] Query regeneration
- 목적: Query에 따라 달라지는 점수 비교
- 방법:
    - User Query(Baseline)
    - Keywords extraction ⛏️
    - convert to Document format
- 평가 지표:
    - Precision
    - Recall (main)
    - F1 score

### 📌 [2] search
- 목적: Search Algorithm에 따라 달라지는 점수 비교
- 방법:
    - BM25
    - Dense Search ⛏️
    - Hybrid
    - LLM Reranker
- 평가 지표:
    - Precision
    - Recall (main)
    - F1 score