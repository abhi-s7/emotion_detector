"""
Flask server for Emotion Detector web application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Receives text from the user, runs emotion detection, and returns formatted results.
    Handles blank input and invalid text.
    """
    text_to_analyze = request.args.get('textToAnalyze', '').strip()
    if not text_to_analyze:
        return 'Invalid text! Please try again!'

    response = emotion_detector(text_to_analyze)

    # Error handling for None dominant_emotion
    if response.get('dominant_emotion') is None:
        return 'Invalid text! Please try again!'

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    """Renders the main index page."""
    return render_template("index.html")

def run_app():
    """Runs the Flask application on localhost:5000."""
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run_app()
# Your code has been rated at 10.00/10 (previous run: 7.83/10, +2.17)
