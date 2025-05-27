from google import genai
from google.genai import types
import base64

def generate(doc,prompt,maxtokens=10):
        client = genai.Client(
            vertexai=True,
            # fill your project id
            project="qwiklabs-gcp-01-3285111e9bbe",
            # fill your location
            location="global",
        )

        msg1_text1 = types.Part.from_text(text=doc)
        si_text1 = prompt

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
            max_output_tokens = maxtokens,
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
            print(result)
            try:
                result=result+" "+chunk.text
            except:
                pass
        return result