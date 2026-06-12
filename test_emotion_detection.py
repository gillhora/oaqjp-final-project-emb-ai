import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy_dominant(self):
        self.assertEqual(emotion_detector("I am glad this happened")['dominant_emotion'], 'joy')

    def test_anger_dominant(self):
        self.assertEqual(emotion_detector("I am really mad about this")['dominant_emotion'], 'anger')

    def test_disgust_dominant(self):
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'], 'disgust')

    def test_fear_dominant(self):
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant_emotion'], 'fear')

    def test_sadness_dominant(self):
        self.assertEqual(emotion_detector("I am so sad about this")['dominant_emotion'], 'sadness')

if __name__ == '__main__':
    unittest.main()
