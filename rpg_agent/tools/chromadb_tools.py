from chromadb import Documents, EmbeddingFunction, Embeddings
import chromadb
from google import genai
from google.genai import types
import os

genai_client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# for m in genai_client.models.list():
#     if "embedContent" in m.supported_actions:
#         print(m.name)

class GeminiEmbeddingFunction(EmbeddingFunction):
    document_mode = True
    def __call__(self, input: Documents) -> Embeddings:
        if self.document_mode:
            embedding_task = "retrieval_document"
        else:
            embedding_task = "retrieval_query"

        response = genai_client.models.embed_content(
            model="models/gemini-embedding-001",
            contents=input,
            config=types.EmbedContentConfig(
                task_type=embedding_task,
            ),
        )

        return [e.values for e in response.embeddings]
    

os.makedirs(os.getenv("CHROMADB_PATH"),exist_ok=True)
chroma_client = chromadb.PersistentClient(path=os.getenv("CHROMADB_PATH"))

DB_NAME = "rpgdata"
embed_fn = GeminiEmbeddingFunction()
embed_fn.document_mode = True
try:
    try:
        db = chroma_client.get_collection(name=DB_NAME,embedding_function=embed_fn)
    except:
        db = chroma_client.create_collection(name=DB_NAME,embedding_function=embed_fn)
except:
    raise Exception("Unable to initialize chromadb")


def db_query(query:str, n_results:int) -> list[tuple[str,str]]:
    """Look up the results in chromadb collection most similar to the query
    where n_results is the number of results to retrieve.
    
    Returns:
        List of documents and corresponding ids, where each entry is a tuple (id, document)
        The tuple can be accessed to get the id and document
    """
    print(f"CALL: db_query on {query}")
    result = db.query(query_texts=[query], n_results=n_results,
                      include=["documents", "metadatas"])
    [all_ids] = result["ids"]
    [all_passages] = result["documents"]
    print(f"FINISH: db_query")
    return list(zip(all_ids,all_passages))

def db_insert(document:str) -> None:
    """Add document to chroma db
    
    Returns None
    """
    db.add(documents=[document],ids=[str(db.count() + 1)])

    


