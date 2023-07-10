"""
This is the main functionality module to generate sentiment detection using OpenAI API.
"""

# Import the dependencies
import openai
from configobj import ConfigObj

# Set up the configurations
config_obj = ConfigObj("config_gpt_detector.ini")
openai_api_key = config_obj["OPENAI"]["openai_api_key"]
openai.api_key = openai_api_key


# GPT Emotion Detector function
def gpt_detect_sentiment(prompt, emotions):
    """
    This is sentiment detection function
    :param prompt: The text to detect the sentiment
    :param emotions: The different emotional categories to classify a prompt on
    :return: The output sentiment.
    """
    sys_prompt = f"""
    You are an emotionally intelligent assistant.
    Classify the sentiment of the user"s text with ONLY ONE OF THE FOLLOWING EMOTIONS: {emotions}.
    After classifying the text, respond with the emotion ONLY.
    """

    messages = [
        {
            "role": "system",
            "content": sys_prompt
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=20,
        temperature=0
    )

    content = response.choices[0].message.content
    if content == "":
        return "N/A"
    return content
