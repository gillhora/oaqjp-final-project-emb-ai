import requests
import json

def emotion_detector(text_to_analyse): # Define a function named emotion_detector that takes a string input (text_to_analyse) 
    ''' This functioin receives a text to be analyzed.
        It returns a dictionary with label and score.
    '''

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the sentiment analysis service 
    myobj = { "raw_document": { "text": text_to_analyse } } # Create a dictionary with the text to be analyzed 
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" } # Set the headers required for the API request 
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers 

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        formatted_response = json.loads(response.text)

        data = [
                (formatted_response['emotionPredictions'][0]['emotion']['anger'], "anger"),
                (formatted_response['emotionPredictions'][0]['emotion']['disgust'], "disgust"),
                (formatted_response['emotionPredictions'][0]['emotion']['fear'], "fear"),
                (formatted_response['emotionPredictions'][0]['emotion']['joy'], "joy"),
                (formatted_response['emotionPredictions'][0]['emotion']['sadness'], "sadness")
        ]
        dominant_emotion = max(data, key=lambda item: item[0])[1]
        return {
                'anger': data[0][0],
                'disgust': data[1][0],
                'fear': data[2][0],
                'joy': data[3][0],
                'sadness': data[4][0],
                'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
        }
    else:
        return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
        }
