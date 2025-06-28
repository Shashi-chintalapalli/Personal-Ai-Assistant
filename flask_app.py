import os
from flask import Flask, render_template, request, jsonify
from assistant.get_response import get_gpt_reply

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    query = request.json["query"]
    response = get_gpt_reply(query)
    return jsonify({"response": response})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render sets PORT
    app.run(host='0.0.0.0', port=port)




