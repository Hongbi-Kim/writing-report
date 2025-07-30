import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from langchain_docling import DoclingLoader
from langchain_docling.loader import ExportType

FILE_PATH = "../data/RFP3.pdf"

# 시간 오래 걸림
# 내부적으로 레이아웃을 파싱하고, LLM이 이해하기 쉽게 Rule-Based로 수행.
loader = DoclingLoader(
    file_path = FILE_PATH,
    export_type = ExportType.MARKDOWN
)

docs = loader.load()

from langchain_text_splitters import MarkdownHeaderTextSplitter

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "Header_1"),
        ("##", "Header_2"),
        ("###", "Header_3"),
    ]
)
splits = [split for doc in docs for split in splitter.split_text(doc.page_content)]

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "Header_1"),
        ("##", "Header_2"),
        ("###", "Header_3"),
    ],
    strip_headers = False
)

splits_with_header = [split for doc in docs for split in splitter.split_text(doc.page_content)]

for d in splits[:3]:
    print(f"- {d.page_content=}")
print("...")

header = ", ".join([splits_with_header[i].page_content.replace(splits[i].page_content, "") for i in range(len(splits))])

from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model = "bge-m3:latest",
)

from langchain_qdrant import QdrantVectorStore
from langchain_qdrant import RetrievalMode

vector_store = QdrantVectorStore.from_documents(
    documents=splits,
    embedding = embeddings,
    location = ":memory:",
    collection_name = "rag_collection",
    retrieval_mode = RetrievalMode.DENSE
)

