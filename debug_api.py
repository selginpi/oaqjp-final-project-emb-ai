import requests
import json

def debug_emotion_api():
    """Debug function to test the Watson NLP API"""
    
    test_texts = [
        "I am so happy today!",
        "I am really mad about this!",
        "I feel so sad about the news.",
        "I am terrified of what might happen.",
        "This food tastes disgusting!"
    ]
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    for text in test_texts:
        print(f"\n{'='*50}")
        print(f"Testing: '{text}'")
        print(f"{'='*50}")
        
        payload = {
            "raw_document": {
                "text": text
            }
        }
        
        try:
            print(f"Making request to: {url}")
            response = requests.post(url, json=payload, headers=headers)
            
            print(f"Status Code: {response.status_code}")
            print(f"Response Headers: {dict(response.headers)}")
            print(f"Response Text: {response.text[:500]}")  # First 500 chars
            
            if response.status_code == 200:
                result = response.json()
                print("\nParsed JSON structure:")
                print(json.dumps(result, indent=2))
                
                # Try to extract emotions if they exist
                if 'emotion_predictions' in result:
                    emotions = result['emotion_predictions'][0]['emotion']
                    print(f"\nExtracted emotions: {emotions}")
                    
                    # Find dominant emotion
                    dominant = max(emotions, key=emotions.get)
                    print(f"Dominant emotion: {dominant}")
                else:
                    print("No 'emotion_predictions' in response")
                    print(f"Available keys: {list(result.keys())}")
            else:
                print(f"Error: API returned status {response.status_code}")
                
        except Exception as e:
            print(f"Exception: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    debug_emotion_api()
