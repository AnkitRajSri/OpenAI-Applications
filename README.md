# GPT Sentiment Detector

![](files/sentiments_ai.jpeg)

The GPT Sentiment Detector App contains the following modules:
* A `notebooks` module which contains the analysis work saved in a jupyter notebook, `SentimentDetectorChatGPT.ipynb`.
* A `detector` module which contains the functionality to detect sentiment of a text prompt saved in `sentiment_detector.py`.
* An `app.py` file which contains the web app view, built using streamlit.

## Project setup
* Create an account on the OpenAI platform, https://platform.openai.com/.
* Create an API Secret Key and store in a safe location.
* Install the dependencies, stored in the requirements file, `requirements.txt`.
```commandline
pip install -r requirements.txt
```

## Execution
Run the below command to start the `gpt-sentiment-detector-app`.
```commandline
python3 -m streamlit run app.py
```
