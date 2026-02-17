import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def test_emotion_detector_joy(self):
        """Test joy emotion detection"""
        result = emotion_detector("I am so happy today!")
        self.assertEqual(result['dominant_emotion'], 'joy')
        
    def test_emotion_detector_anger(self):
        """Test anger emotion detection"""
        result = emotion_detector("I am really mad about this!")
        self.assertEqual(result['dominant_emotion'], 'anger')
        
    def test_emotion_detector_sadness(self):
        """Test sadness emotion detection"""
        result = emotion_detector("I feel so sad about the news.")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        
    def test_emotion_detector_fear(self):
        """Test fear emotion detection"""
        result = emotion_detector("I am terrified of what might happen.")
        self.assertEqual(result['dominant_emotion'], 'fear')
        
    def test_emotion_detector_disgust(self):
        """Test disgust emotion detection"""
        result = emotion_detector("This food tastes disgusting!")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        
    def test_empty_input(self):
        """Test empty input handling"""
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        
    def test_blank_input(self):
        """Test blank input handling"""
        result = emotion_detector("   ")
        self.assertIsNone(result['dominant_emotion'])

if __name__ == '__main__':
    unittest.main()
