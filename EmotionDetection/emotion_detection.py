import requests # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze): # Define a function named emotion_detector that takes a string input (text_to_analyze) 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the emotion detector service 
    myobj = { "raw_document": { "text": text_to_analyze } } # Create a dictionary with the text to be analyzed 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request 
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers 
    formatted_response = json.loads(response.text)
    pred = formatted_response['emotionPredictions'][0]['emotion'] 
    anger = pred['anger'] 
    disgust = pred['disgust']
    fear = pred['fear'] 
    joy = pred['joy']
    sadness = pred['sadness'] 
    emotion_scores={'anger' : anger, 'disgust' : disgust, 'fear' : fear, 'joy': joy, 'sadness' : sadness }
    dominant_emotion=max(emotion_scores,key=emotion_scores.get)
    result={'anger' : anger, 'disgust' : disgust, 'fear' : fear, 'joy': joy, 'sadness' : sadness, 'dominant_emotion': dominant_emotion }
    return result
    