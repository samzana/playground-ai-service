from langchain_community.document_loaders import PyPDFLoader 

import os 
def load_documents(file_paths):
    documents = []
    for file_path in file_paths:
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        documents.extend(docs)
    return documents

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
games_pdf_path = os.path.join(BASE_DIR, 'static', 'Playground_Socrates_RAG_Document.pdf')
COMMON_DOCUMENTS = [games_pdf_path]


def get_combined_documents(task_type):
    if task_type == "coding assistant":
        return load_documents(COMMON_DOCUMENTS)
    else: 
        raise ValueError("Invalid task type. Must be 'coding assistant")