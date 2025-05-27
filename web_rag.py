from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_transformers import Html2TextTransformer
from sentence_transformers import SentenceTransformer
import faiss
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def webrag(doc,query):
    # 1. Load & clean webpage content
    def load_and_clean(url):
        loader = WebBaseLoader(url)
        docs = loader.load()
        transformer = Html2TextTransformer()
        clean_docs = transformer.transform_documents(docs)
        text = clean_docs[0].page_content
        return text

    # 2. Chunk text with overlap
    def chunk_text(text, chunk_size=150, overlap=50):
        words = text.split()
        chunks = []
        start = 0
        while start < len(words):
            end = min(start + chunk_size, len(words))
            chunks.append(" ".join(words[start:end]))
            start += chunk_size - overlap
        return chunks

    # 3. Build FAISS index from chunks
    def build_faiss_index(chunks, embed_model):
        embeddings = embed_model.encode(chunks, convert_to_numpy=True)
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)
        return index, embeddings

    # 4. Retrieve top-k relevant chunks for a query
    def retrieve_chunks(query, embed_model, index, chunks, k=3):
        q_emb = embed_model.encode([query])
        _, idxs = index.search(q_emb, k)
        return [chunks[i] for i in idxs[0]]

    # # 5. Generate answer with HuggingFace causal LM
    # def generate_answer(context, query, model_name="tiiuae/falcon-rw-1b"):
    #     prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    #     tokenizer = AutoTokenizer.from_pretrained(model_name)
    #     model = AutoModelForCausalLM.from_pretrained(model_name)
    #     generator = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=100)
    #     output = generator(prompt)[0]["generated_text"]
    #     return output

    # ----------- USAGE ------------

    # url = "https://medium.com/@zhonghong9998/attention-mechanisms-in-deep-learning-enhancing-model-performance-32a91006092a"
    # text = load_and_clean(url)
    chunks = chunk_text(doc, chunk_size=150, overlap=50)

    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
    index, embeddings = build_faiss_index(chunks, embed_model)

    # query = "Who is the author?"
    retrieved = retrieve_chunks(query, embed_model, index, chunks, k=3)
    context = "\n".join(retrieved)

    # answer = generate_answer(context, query)
    # print("\n--- Answer ---\n", answer)
    # print(context)

    prompt=f"Answer the question based on the context below:\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"
    return prompt