from flask import Flask, request, jsonify, render_template
import os
import random
import requests
import json

responses = ("What?", "Not feeling to goood", "Hey hey hey", "I am a fullstack developer", "Im so drunk!", "Nice!")

app = Flask(__name__)

# communicating with others
app = Flask(__name__)
@app.route("/message/")
def message():
    if request.args.get('message'):
        user_input = request.args.get('message')
        response = requests.get("https://immense-thicket-73815.herokuapp.com/message/?message=" + user_input)
        json_string = json.loads(response.content)
        response_message = {json_string["message"]}
        return str(response_message)
    else:
        return 'Please write "message=" in the URL ... '


# parrot
app = Flask(__name__)
@app.route("/message/")
def message():
    message = request.args.get('message')
    return message


# drunk
app = Flask(__name__)
@app.route("/message/")
def message():
    if request.args.get('message'):
        return random.choice(responses)
    else:
        return "message = "


if __name__ == "__main__":
    local = "127.0.0.1"
    heroku = "0.0.0.0"
    port = int(os.environ.get("PORT", 5000))
    app.run(host=heroku, port=port)
