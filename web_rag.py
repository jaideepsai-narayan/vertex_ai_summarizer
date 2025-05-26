from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_transformers import Html2TextTransformer
# from transformers import AutoTokenizer,AutoModelForCausalLM,pipeline,TextStreamer

from vertexai import rag
from vertexai.generative_models import GenerativeModel, Tool
import vertexai

import os
import sys

# pip install --upgrade google-genai
# gcloud auth application-default login

def out(urls):
    
    loader = WebBaseLoader(urls)
    docs = loader.load()
    html2text = Html2TextTransformer()
    docs_transformed = html2text.transform_documents(docs)
    # print(docs_transformed[0].page_content[0:500])
    doc=docs_transformed[0].page_content
    
    filename = "inp.txt"
    
    append_string = docs
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} existed and has been removed.")
    else:
        with open(filename, "a") as f:
            f.write(append_string)
        print(f"{filename} did not exist. String appended.")
      
    # Initialize Vertex AI API once per session
    vertexai.init(project="project_id", location="location")
    
    # Direct context retrieval
    rag_retrieval_config = rag.RagRetrievalConfig(
        top_k=3,  # Optional
        filter=rag.Filter(vector_distance_threshold=0.5),  # Optional
    )

    # Enhance generation
    # Create a RAG retrieval tool
    rag_retrieval_tool = Tool.from_retrieval(
        retrieval=rag.Retrieval(
            source=rag.VertexRagStore(
                rag_resources=[
                    rag.RagResource(
                        rag_corpus=filename,  # Currently only 1 corpus is allowed.
                        # Optional: supply IDs from `rag.list_files()`.
                        # rag_file_ids=["rag-file-1", "rag-file-2", ...],
                    )
                ],
                rag_retrieval_config=rag_retrieval_config,
            ),
        )
    )

    # Create a Gemini model instance
    rag_model = GenerativeModel(
        model_name="gemini-2.0-flash-001", tools=[rag_retrieval_tool]
    )
    
    # Generate response
    prompt="""
    You are an expert AI assistant to summarize the documents.
    Your primary goal is to help underwriters by accurately and concisely summarizing client information and highlighting potential risk factors.
    Maintain a professional and objective tone.
    Focus only on the information provided in the prompt. Do not invent details.
    """
    response = rag_model.generate_content(prompt)
    return response.text
    
    
    
