import html

import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

LANGUAGES = {
    "en": "English",
    "ta": "Tamil",
    "hi": "Hindi",
    "te": "Telugu",
    "ml": "Malayalam",
    "kn": "Kannada",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "ar": "Arabic",
    "ja": "Japanese",
}


@app.get("/")
def home():
    return render_template("index.html", languages=LANGUAGES)


@app.post("/translate")
def translate():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify(error="Invalid request."), 400

    text = data.get("text", "")
    source = data.get("source")
    target = data.get("target")

    if not isinstance(text, str) or not text.strip():
        return jsonify(error="Please enter text to translate."), 400

    text = text.strip()

    if source not in LANGUAGES or target not in LANGUAGES:
        return jsonify(error="Please select valid languages."), 400

    if len(text.encode("utf-8")) > 500:
        return jsonify(
            error="Text is too long. Please use a shorter sentence (maximum 500 bytes)."
        ), 400

    if source == target:
        return jsonify(translation=text)

    try:
        response = requests.get(
            "https://api.mymemory.translated.net/get",
            params={"q": text, "langpair": f"{source}|{target}"},
            timeout=20,
        )
        response.raise_for_status()
        result = response.json()

        if str(result.get("responseStatus")) != "200":
            return jsonify(
                error="The translation service could not translate this text. "
                      "Try again later or choose another language pair."
            ), 502

        translated = result.get("responseData", {}).get("translatedText")

        if not isinstance(translated, str) or not translated.strip():
            return jsonify(error="No translation was returned."), 502

        return jsonify(translation=html.unescape(translated))

    except requests.Timeout:
        return jsonify(error="Translation timed out. Please try again."), 504

    except (requests.RequestException, ValueError):
        return jsonify(
            error="Cannot reach the translation service. Check your internet connection."
        ), 502


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)