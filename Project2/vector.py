from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader


def get_retriever(
    embedding_model_name: str = "text-embedding-ada-002",
    collection_name: str = "default_collection",
    search_type: str = "similarity",
    k: int = 10,
):
    """
    Creates and returns a retriever object using the given documents and embedding model.

    Args:
        documents (list): List of LangChain Document objects or text chunks.
        embedding_model_name (str): Name of the OpenAI embedding model to use.
        collection_name (str): Name of the Chroma collection.
        search_type (str): Type of search (e.g., 'similarity', 'mmr').
        k (int): Number of results to retrieve.

    Returns:
        retriever: Configured retriever object.
    """
    try:
        documents = get_chunks()
        # Create embedding model
        embedding_model = OpenAIEmbeddings(model=embedding_model_name)

        # Create and store document embeddings in Chroma vectorstore
        vectorstore = Chroma.from_documents(
            documents, embedding_model, collection_name=collection_name
        )

        # Create and return retriever
        retriever = vectorstore.as_retriever(
            search_type=search_type, search_kwargs={"k": k}
        )

        print(
            f"[INFO] Retriever created successfully (k={k}, search_type={search_type})"
        )
        return retriever

    except Exception as e:
        print(f"[ERROR] Failed to create retriever: {e}")
        return None


def get_chunks():
    loader = TextLoader("filters.txt", encoding="utf-8")

    # Define the text splitter (same as before)
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base", chunk_size=512, chunk_overlap=16
    )

    # Load and split into chunks
    filter_chunks = loader.load_and_split(text_splitter)

    return filter_chunks
