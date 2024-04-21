"""
This module implements a Flask server for emotion detection.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotional Detector")

@app.route("/emotionDetector")
def emotion_detectors():
    """
    Handle emotion detection requests.

    Retrieves the text to analyze from the request arguments and returns
    the emotion detection results.

    Returns:
    str: The system response for the given statement.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    response_str = "For the given statement, the system response is "
    for key, value in result.items():
        response_str += f"'{key}': {value}, "
    response_str = response_str[:-2]  # Remove the trailing comma and space
    response_str += f". The dominant emotion is {result['dominant_emotion']}."
    return response_str
@app.route("/")
def index():
    """
    Return HTML
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
