"""
Emotion detection module for analyzing text using Watson NLP API.
"""

import json
import requests

def emotion_detector(text_to_analyse):
    """
    Calls Watson NLP API to detect emotions in the given text.
    Returns a dictionary of emotion scores and the dominant emotion.
    Handles blank or invalid input by returning None values.
    """
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers=headers, json=payload, timeout=10)

    if response.status_code == 400:
        # Return None for all values if blank or invalid input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    if response.status_code == 200:
        result = json.loads(response.text)
        emotions = result['emotionPredictions'][0]['emotion']
        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)
        emotion_scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    return {"error": response.text}
# Your code has been rated at 10.00/10 (previous run: 7.62/10, +2.38)
