# Repository for Final project
# Emotion Detection Web Application

A Flask-based web application that analyzes text and detects emotions using the Watson NLP Emotion Detection API.

## Features
- Detects five emotions: anger, disgust, fear, joy, and sadness
- Identifies the dominant emotion in a given text
- Handles blank/invalid input gracefully
- Simple and intuitive web interface

## Project Structure
final_project/
 ├── server.py
 ├── templates/
 │    └── index.html
 └── EmotionDetection/
      ├── __init__.py
      └── emotion_detection.py

## Installation

1. Clone the repository:
git clone https://github.com/yvonne123456789/oaqjp-final-project-emb-ai.git

2. Install the required packages:
pip install flask requests

## Usage

1. Start the server:
python3 server.py

2. Open your browser and navigate to:
http://localhost:5000

3. Enter a statement in the text box and click **Analyze**

## Example Output
For the given statement, the system response is 'anger': 0.006274985,
'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and
'sadness': 0.049744144. The dominant emotion is joy.

## API Endpoint
GET /emotionDetector?textToAnalyze=your+text+here

## Technologies Used
- Python 3.11
- Flask
- Watson NLP Emotion Detection API
- HTML/JavaScript

## License
This project is licensed under the MIT License.
