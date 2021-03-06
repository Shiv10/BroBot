import requests
import random
from misc.text import subreddits, meme_api
from telegram.ext import CommandHandler


def meme(update, context):
    options = subreddits
    choice = random.choice((options + ["all"]))
    api = meme_api + choice
    response = requests.get(api).json()
    if choice == "all":
        while response["subreddit"] in options:
            response = requests.get(api).json()
    update.message.reply_photo(response["url"], caption=response["title"])


meme_handler = CommandHandler("meme", meme)
