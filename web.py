from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_transformers import Html2TextTransformer
# from transformers import AutoTokenizer,AutoModelForCausalLM,pipeline,TextStreamer

from google_model import generate
from web_rag import webrag

# pip install --upgrade google-genai
# gcloud auth application-default login
global doc_text
doc_text=""

def out(urls):
    global doc_text

    loader = WebBaseLoader(urls)
    docs = loader.load()
    html2text = Html2TextTransformer()
    docs_transformed = html2text.transform_documents(docs)
    # print(docs_transformed[0].page_content[0:500])
    doc=docs_transformed[0].page_content
    doc_text=doc
    prompt="""
    You are an expert AI assistant to summarize the documents.
    Your primary goal is to help underwriters by accurately and concisely summarizing client information and highlighting potential risk factors.
    Maintain a professional and objective tone.
    Focus only on the information provided in the prompt. Do not invent details.
    """
    return generate(doc,prompt,2000)

def rag_qa(query):
    
    context=webrag(doc_text,query)
    prompt="""
    You are an expert AI assistant to answer questions based on the input context.
    Maintain a professional and objective tone.
    Focus only on the information provided in the prompt. Do not invent details.
    """
    return generate(context,prompt,100)






