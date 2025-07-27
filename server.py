from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
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
    return render_template("index.html")

def run_app():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run_app()