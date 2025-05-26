from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_transformers import Html2TextTransformer
# from transformers import AutoTokenizer,AutoModelForCausalLM,pipeline,TextStreamer

from google import genai
from google.genai import types
import base64


# pip install --upgrade google-genai
# gcloud auth application-default login

def out(urls):
    
    loader = WebBaseLoader(urls)
    docs = loader.load()
    html2text = Html2TextTransformer()
    docs_transformed = html2text.transform_documents(docs)
    # print(docs_transformed[0].page_content[0:500])
    doc=docs_transformed[0].page_content

    def generate(doc):
        client = genai.Client(
            vertexai=True,
            # fill your project id
            project="<your_project_id>",
            # fill your location
            location="<your_location>",
        )

        msg1_text1 = types.Part.from_text(text=doc)
        si_text1 = """You are an expert AI assistant to summarize the documents.
        Your primary goal is to help underwriters by accurately and concisely summarizing client information and highlighting potential risk factors.
        Maintain a professional and objective tone.
        Focus only on the information provided in the prompt. Do not invent details."""

        model = "gemini-2.5-flash-preview-05-20"
        contents = [
            types.Content(
            role="user",
            parts=[
                msg1_text1
            ]
            ),
        ]

        generate_content_config = types.GenerateContentConfig(
            temperature = 0.1,
            top_p = 1,
            seed = 0,
            max_output_tokens = 65535,
            safety_settings = [types.SafetySetting(
            category="HARM_CATEGORY_HATE_SPEECH",
            threshold="OFF"
            ),types.SafetySetting(
            category="HARM_CATEGORY_DANGEROUS_CONTENT",
            threshold="OFF"
            ),types.SafetySetting(
            category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
            threshold="OFF"
            ),types.SafetySetting(
            category="HARM_CATEGORY_HARASSMENT",
            threshold="OFF"
            )],
            system_instruction=[types.Part.from_text(text=si_text1)],
        )

        result=""

        for chunk in client.models.generate_content_stream(
            model = model,
            contents = contents,
            config = generate_content_config,
            ):
            # print(chunk.text, end="")
            result=result+" "+chunk.text
        return result

    return generate(doc)
