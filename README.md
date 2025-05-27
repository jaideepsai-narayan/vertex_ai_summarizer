
# 🧠 Chrome Extension for AI Summarization Using Vertex AI + RAG

A powerful and user-friendly Chrome extension that lets you chat with any web page and ask questions directly about its content. Powered by Google Cloud's Vertex AI and the Gemini 2.5 Flash model, it enables intelligent, context-aware conversations with articles, research papers, blogs, and more — without ever leaving the page.

This project brings real-time question-answering and contextual summarization right into your browser, helping you understand complex or lengthy content effortlessly using cutting-edge AI.

### Implemented with Retrieval-Augmented Generation (RAG):

	•	Chunking: Divide the webpage content into meaningful sections.
	•	Embedding: Convert these chunks into vector representations using embedding models.
	•	Storage: Store embeddings in a vector database like FAISS
	•	Retrieval: On user queries, retrieve relevant chunks and generate responses using a language model.
	•	Benefits: Provides more contextually relevant and accurate summaries or answers.

---

## 🚀 Features

- ✨ **AI-Powered Summarization**  
  Uses Google's Vertex AI language models to generate high-quality summaries.
  
- 💬 **RAG Question-Answering**  
  Ask questions directly about the page you're reading

- 🖱️ **One-Click Summary**  
  Simple and intuitive Chrome toolbar button for instant access.

- 🌐 **Real-Time Web Integration**  
  Works seamlessly on any web page without disrupting user experience.

- 💡 **Clarity and Efficiency**  
  Designed to reduce reading time while retaining essential insights.


- **Generated output:**


 <img src="https://github.com/user-attachments/assets/3b81b25e-9c45-4a33-8991-c9dbca605205" width="700"/>



- **Backend generated output:**


<img src="https://github.com/user-attachments/assets/058ba657-f608-4619-bda7-f14a012e27cd" width="700"/>

## 🛠️ Tech Stack

- **Frontend**: JavaScript, HTML, CSS, Chrome Extensions API  
- **Backend**: Google Cloud Vertex AI, RESTful APIs  
- **Authentication**: OAuth 2.0 (if implemented for user-specific API access)

## 🎯 Use Cases

- Quickly digest long research papers or academic articles  
- Extract highlights from technical blogs or reports  
- Get summaries of current news without reading entire articles  
- Ideal for students, professionals, and busy readers

---
## 🧑‍💻 Getting Started — Without RAG

### Prerequisites
- [Google Cloud](https://cloud.google.com/) account with Vertex AI enabled
- Chrome browser

### Environment Setup:

```
conda create -n vertex_ai python==3.10
conda activate vertex_ai
```

```
git clone https://github.com/jaideepsai-narayan/vertex_ai_summarizer.git
```

```
cd vertex_ai_summarizer
pip install -r requirements.txt
```

```
gcloud auth application-default login
```


Click on Extensions-->Manage extensions-->Load Unpacked.
Here just open the repository that you cloned. So you can see the extension has been added as shown below.

Load the extension into Chrome:

- Go to chrome://extensions

- Enable "Developer mode"

- Click "Load unpacked"

- Select the project directory


<img src="https://github.com/user-attachments/assets/11d4c239-5b79-4610-994a-541ed64f6728" width="700"/>


### NOTE :

In [google_model.py](./google_model.py) please update your **project** and **location** as shown in the below screenshot.

<img src="https://github.com/user-attachments/assets/6af584e5-6d1d-422d-bba1-d45f7f3ca1d8" width="700"/>



### Running:
Just run server.py file to launch flask.
```
python server.py
```
Now open chrome and click on URL Sender Extension and click on Send URL button.

---
### 🙌 Contributions
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

### 📫 Contact
Created by [Jaideep Sai Narayan](https://github.com/jaideepsai-narayan)
Feel free to reach out via GitHub Issues or [LinkedIn!](https://in.linkedin.com/in/jaideep-sai-narayan-kamisetti-06312018b)

