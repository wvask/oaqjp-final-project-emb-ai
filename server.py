"""
Flask server for the Emotion Detection web application.

This module defines the routes required to render the index page
and process emotion detection requests using the EmotionDetection package.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Render the main index page.

    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Process the emotion detection request.

    Retrieves user input from the query string, calls the
    emotion_detector function, and returns a formatted response.

    Returns:
        str: Formatted emotion analysis result or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
