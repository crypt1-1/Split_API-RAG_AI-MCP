import chromadb

from config import config.py-path

client = chromadb.PersistentClient(path=chroma-path)

collection = client.get_or_create_collection(
    name="docs"
)


def search_rag(query, n_results=5):

    result = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return result
