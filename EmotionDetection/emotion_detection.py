import requests
import json

def emotion_detector(text_to_analyze):
    """Analyze text and return emotion scores with dominant emotion"""
    
    # Handle blank input
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Watson NLP API endpoint and model
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # Prepare the request payload
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    try:
        # Make the POST request
        response = requests.post(url, json=myobj, headers=headers)
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse the JSON response
            result = response.json()
            
            # Extract emotion scores - using 'emotionPredictions' (capital P)
            emotions = result['emotionPredictions'][0]['emotion']
            
            # Extract individual scores
            anger_score = emotions['anger']
            disgust_score = emotions['disgust']
            fear_score = emotions['fear']
            joy_score = emotions['joy']
            sadness_score = emotions['sadness']
            
            # Find dominant emotion
            scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            dominant_emotion = max(scores, key=scores.get)
            
            # Return formatted output
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        else:
            # Handle non-200 status codes
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
            
    except requests.exceptions.RequestException:
        # Handle network errors
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    except KeyError:
        # Handle JSON parsing errors
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
