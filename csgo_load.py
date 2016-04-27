import urllib, urllib2
import json

# Save the output of this link
# http://csgolyzer.com/api/items?api_key=
# to a file called items

items = open("items","r")
items_string = items.read()
items.close()
object_json = json.loads(items_string)['items']

weapon_file = open("weapons.txt", "w")

for item in object_json:
	try:
		if item['icon_url'] != '':
			weapon_file.write(item['market_hash_name'] + "," + item['icon_url']  +"\n")
		else:
			weapon_file.write(item['market_hash_name'] + ",nope\n")
	except:
		pass # Special symbols are not allowed

weapon_file.close()
