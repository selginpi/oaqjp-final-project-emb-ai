from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """Handle emotion detection requests"""
    # Get the text from the request
    data = request.get_json()
    text_to_analyze = data.get('text', '')
    
    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)
    
    # Check if result is valid (dominant_emotion is not None)
    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid input! Please try again."}), 400
    
    # Format the response
    response = {
        "text": text_to_analyze,
        "anger": result['anger'],
        "disgust": result['disgust'],
        "fear": result['fear'],
        "joy": result['joy'],
        "sadness": result['sadness'],
        "dominant_emotion": result['dominant_emotion']
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
