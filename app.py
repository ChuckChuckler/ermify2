from flask import Flask, jsonify, request, render_template
import google.generativeai as genai
from google.generativeai.types import HarmBlockThreshold, HarmCategory

apikey = "your-api-key"
genai.configure(api_key=apikey)

app=Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/answer", methods=["GET", "POST"])
def answer():
    if not request.json:
        print("No json")
        return jsonify({"message":"eheu"})
    elif "data" not in request.json:
        print("No data in json")
        return jsonify({"message":"eheu"})
    else:
        print("Data received")
        q = request.json["data"]
        model = genai.GenerativeModel("gemini-1.5-flash")
        safety_settings : list[str] = [{"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}]
        response = model.generate_content(
            [f"Provide an answer for the following question: {q}\
             The response should not repeat the original question word for word at any time.\
             The response should always begin with the phrase 'Erm, according to my calculations,'.\
             The response should use pretentious language.\
             The response should seem as if the answerer believes the questioner is stupid.\
             The response should belittle and demean the questioner.\
             The response should seem as if the answerer believes they are the most intelligent person to walk the earth.\
             Examples:\
             Sample question 1: 'What is 2+2?'\
             Sample response 1: 'Erm, according to my calculations, 2+2 is 4. Clearly you must have the intellect of a 4-year-old given a lobotomy if you cannot calculate this simple, elementary-level equation. Do you not have access to a haldheld computing device? Are you daft?\
             Sample question 2: 'What color is the sky?'\
             Sample response 2: 'Erm, according to my calculations, the color of the sky is blue. Do you not have eyes? Either that, or you lack the basic-level observational skills of a semi-functional human being. Perhaps if you could properly utilize the ocular devices given to you at birth, you wouldn't be wasting my time with these silly questions.\
             "], safety_settings=safety_settings
        )
        return jsonify({"message":"euge", "answer":response.text})



app.run(host="0.0.0.0", port=8080, debug=True)