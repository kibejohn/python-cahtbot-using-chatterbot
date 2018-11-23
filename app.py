# main  are  imports:: flask, chatterbot
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import math

app = Flask(__name__)

mobiBot = ChatBot("Chatterbot")
conv = [
    "Hey Buddy",
    "Whats app",
    "Am cool",
    "Ok cool",
    "Hey There",
    "Hello",
    "I am a friendly chatbot",
    "What is your name?",
]
#Using a training set of a listData(I could have used ChatterBotCorpusTrainer or twittertrainerApi, etc)
mobiBot.set_trainer(ListTrainer)
mobiBot.train(conv)

#return a template to display on webbrowser
@app.route("/")
def home():
    return render_template("index.html")

#get data from user input using name of input tag process it and return result from our bot
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(mobiBot.get_response(userText))

if __name__ == "__main__":
    app.run(port=5050)
