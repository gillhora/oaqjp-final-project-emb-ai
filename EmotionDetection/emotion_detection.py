import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends text to Watson NLP Emotion API and returns a formatted dictionary
    with emotion scores and dominant emotion.
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response_dict = json.loads(response.text)

        # Extract emotion scores
        emotions = response_dict["emotionPredictions"][0]["emotion"]
        
        anger = emotions["anger"]
        disgust = emotions["disgust"]
        fear = emotions["fear"]
        joy = emotions["joy"]
        sadness = emotions["sadness"]

        # Find dominant emotion
        emotion_scores = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness
        }

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return formatted result
        return {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion": dominant_emotion
        }

    except Exception as e:
        return {"error": str(e)}