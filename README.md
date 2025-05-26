## Webpage-summarizer:
- **Description:** 
Chrome extension delivers concise and accurate summaries of webpages. Whether you're reading articles, research papers, or long reports, this extension helps you save time by providing the key points at a glance.

- **frontend generated output:**


 <img src="https://github.com/user-attachments/assets/077d3304-0e82-4692-b390-944827f6bc87" width="700"/>

- **backend generated output:**


<img src="https://github.com/user-attachments/assets/058ba657-f608-4619-bda7-f14a012e27cd" width="700"/>

## Verified Environment:
- [Google Cloud]([https://cloud.google.com/])
- Local Setup

## Environment Setup:

```
https://github.com/jaideepsai-narayan/vertex_ai_summarizer.git
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


<img src="https://github.com/user-attachments/assets/11d4c239-5b79-4610-994a-541ed64f6728" width="700"/>


### NOTE :

In [Web.py]([./web.py]) please update your **project** and **location** as shown in the below screenshot.

<img src="https://github.com/user-attachments/assets/513ee4a7-c5f9-4288-98d6-00af4e402c0f" width="700"/>


## Running:
Just run server.py file to launch flask.
```
python server.py
```
Now open chrome and click on URL Sender Extension and click on Send URL button.
