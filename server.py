''' Executing this function initiates the application to be executed over the Flask channel and deployed on localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Receives text from the HTML interface and runs emotion detection.
    Returns a formatted string with emotion scores and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze', '').strip()
    if not text_to_analyze:
        return 'No text provided. Please enter some text to analyze.'
    
    print(f"Received text for analysis: {text_to_analyze}")

    response = emotion_detector(text_to_analyze)

    print(f"Emotion detection response: {response}")

    if 'error' in response:
        return "Invalid input! Try again."

    # Extract emotion scores
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
    """Renders the main application page."""
    return render_template("index.html")

def run_app():
    """Executes the Flask app and deploys it on localhost:5000."""
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run_app()
