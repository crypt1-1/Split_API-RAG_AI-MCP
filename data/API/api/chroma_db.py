import chromadb

from config import CHROMA_DIR

client = chromadb.PersistentClient(path=CHROMA_DIR)

collection = client.get_or_create_collection(
    name="docs"
)


def search_rag(query, n_results=5):

    result = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return result
