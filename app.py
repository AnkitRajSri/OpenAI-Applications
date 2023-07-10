import streamlit as sl
from app.sentiment_detector import gpt_detect_sentiment


def main():
    col_1, col_2 = sl.columns([0.85, 0.15])
    with col_1:
        sl.title("GPT Sentiment Detector")
    with col_2:
        sl.image("ai.jpg", width=70)

    with sl.form(key="ai_form"):
        default_emotions = "positive, negative, neutral"
        emotions = sl.text_input("Emotions:", value=default_emotions)

        text = sl.text_area(label="Text to classify:")
        submit_button = sl.form_submit_button(label="Detect!")

        if submit_button:
            emotion = gpt_detect_sentiment(text, emotions)
            result = f"{text} => {emotion}\n"
            sl.write(result)

            sl.divider()

            if "history" not in sl.session_state:
                if result:
                    sl.session_state["history"] = result
                else:
                    sl.session_state["history"] = ""
            else:
                sl.session_state["history"] += result

            if sl.session_state["history"]:
                sl.text_area(label="History", value=sl.session_state["history"], height=400)


if __name__ == "__main__":
    main()
