from flask import Flask
import facebot, whatsapp_bot

app = Flask(__name__)

@app.route("/facebot")
def send_facebook():
    return facebot.send_message()

@app.route("/whatsapp")
def send_whatsapp():
    return whatsapp_bot.send_message()