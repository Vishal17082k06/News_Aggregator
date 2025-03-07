from flask import Flask, jsonify
import json
import speech_recognition as sr

News_Aggregator = Flask(__name__)

def load_news(file_path="news_data.json"):
    with open(file_path, "r") as file:
        return json.load(file)

def search_news(query, news_list):
    return [news for news in news_list if query.lower() in news["title"].lower()]

@News_Aggregator.route("/voice-search", methods=["GET"])
def voice_search():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a voice query...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")

        news_list = load_news()
        results = search_news(query, news_list)

        return jsonify({"query": query, "results": results})
    
    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand your voice"}), 400
    except sr.RequestError:
        return jsonify({"error": "Speech recognition service unavailable"}), 500


if __name__ == "__main__":
    News_Aggregator.run(debug=True)    