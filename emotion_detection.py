import requests

def emotion_detector(text):
    ''' This code receives the text from the HTML interface and returns'''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text } }
    response = requests.post(url, headers=headers, json=myobj)
    return response.text

print(emotion_detector("I love python"))