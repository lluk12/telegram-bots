import telebot
import urllib, urllib2
import time
import json

KEY = '172507794:AAHF3PwzoG_YidIrP0yX9GL_pKLHBrhpX1c'
bot = telebot.TeleBot(KEY)

global items
items = []
global images
images = []

def getItemList():
	global items
	global images
	lines = [line.rstrip('\n') for line in open('weapons.txt')]
	for line in lines:
		print line
		items.append(line.split(',')[0])
		images.append(line.split(',')[1])

def getObjects(query):
	global items
	global images
	stop = False
	items_found = []
	query_len = len(query)
	i = 0
	item_counter = 0
	for value in items:
		if query_len > len(value) or stop == True or i > 10:
			break
		if query.lower() == value[:query_len].lower():
			if images[item_counter] != 'nope':
				print "Entra"
				thumb_url = 'http://steamcommunity-a.akamaihd.net/economy/image/' + images[item_counter] + '/62fx62f'
				print thumb_url
				items_found.append(telebot.types.InlineQueryResultArticle(str(i), value, telebot.types.InputTextMessageContent('/get ' + value), thumb_url=thumb_url, thumb_width=62, thumb_height=62))

			else:
				items_found.append(telebot.types.InlineQueryResultArticle(str(i), value, telebot.types.InputTextMessageContent('/get ' + value)))
			i += 1
		elif i > 1:
			stop = True
		item_counter += 1
	return items_found


def getPrices(hash_name):
	params = { 'market_hash_name' : hash_name }
	url = "http://steamcommunity.com/market/priceoverview/?currency=1&appid=730&" + urllib.urlencode(params)
	content = urllib2.urlopen(url).read()
	object_json = json.loads(content)
	if object_json['success'] != True:
		raise Exception
	prices = []
	if 'lowest_price' in object_json:
		prices.append(str(object_json['lowest_price']))
	else:
		prices.append('Not found')
	if 'median_price' in object_json:
		prices.append(str(object_json['median_price']))
	else:
		prices.append('Not found')
	return prices

# This function will be called with the get command
@bot.message_handler(commands=['get'])
def getCommand(message):
	global items
	try:
		hash_name = message.text.split(' ', 1)[1]
	except:
		print "Couldn't get the hash_name"
		bot.send_message(message.chat.id, "Did you add a skin name?")
		return 1
	if hash_name in items:
		try:
			prices = getPrices(hash_name)
			bot.send_message(message.chat.id, "Lowest price of the item: " + prices[0] + ". Median Price is: " + prices[1])
		except Exception as e:
			print "Exepction getting prices: " + e.message
			bot.send_message(message.chat.id, "Couldn't get the price. Maybe the item is not in the marketplace?")
			return 1
	else:
		print "Hash name not in items"
		bot.send_message(message.chat.id, "Couldn't find the item, maybe not supported. It's preferrable to use inline mode")


# This function is executed when someone types text
@bot.inline_handler(lambda query: len(query.query) > 0)
def query_with_text(inline_query):
	query = inline_query.query
	try:
		items_found = getObjects(query)
		bot.answer_inline_query(inline_query.id, items_found)	
	except:
		bot.send_message(message.chat.id, "Problem getting the objects")



def main_loop():
	getItemList()
	bot.polling(True)
	while True:
		time.sleep(3)


if __name__ == '__main__':
	try:
		main_loop()
	except KeyboardInterrupt:
		print >> sys.stderr, '\nExiting by user request.\n'
		sys.exit(0)
