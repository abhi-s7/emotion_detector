import json
import requests

def emotion_detector(text_to_analyse):
    """
    Function to detect emotions from input data.
    """
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }

    print(f"Sending request to {url} with headers {headers} and payload {json.dumps(payload)}")

    response = requests.post(url, headers=headers, json=payload)

    print(f"Received response {response}")

    if response.status_code == 200:
        return response.text
    else:
        return {"error": response.text}