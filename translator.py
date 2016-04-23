# Remember to include the different encodings for the different languages

# Including necessary libraries
# telebot - to use the TelegramBot API
# urrlib2 - to connect to yandex (translator) and make requests
# json - to get the text of the responses
import telebot
import urllib2
import json

# Token of the telegram Bot
TOKEN_TELEGRAM = 'HERE YOU SHOULD ADD YOUR TOKEN'
# Linking the Bot to this python script
bot = telebot.TeleBot(TOKEN_TELEGRAM)

# Token of Yandex API to get the translation
TOKEN_YANDEX = 'HERE YOU SHOULD ADD YOUR TOKEN'

# Function to get the translation given a text.
# Given a Spanish text, creates a request for Yandex and
# returns the translation in English
def getTranslation(text):
	from_language = 'es' # Modify this to change the input language (es, en, ru,...)
	to_language = 'en' # Modify this to change the output language
	languages = from_language + '-' + to_language
	url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
	params = { 'key' : TOKEN_YANDEX, 'text' : str(text), 'lang' : languages }
	url += urllib.urlencode(params)
	content = urllib2.urlopen(url).read()
	object_json = json.loads(content)
	return object_json['text']


# If you want to add commands, you should do it like this function
#@bot.message_handler(commands=['start', 'help'])
#def send_welcome(message):
#	pass
#


# Function that will handle all incoming messages.
# It will call the function to create the translation
# and will send a message to the user with the translation
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
	text = getTranslation(message.text)
	bot.reply_to(message, text)

# Function that starts the bot-telegram connection
bot.polling()
