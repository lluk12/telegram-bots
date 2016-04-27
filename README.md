# telegram-bots

Repository to upload bots for the Telegram app. Everyone is free to take any of the bots and modify them.

### translator

Bot that will translate a text entered in the chat using the yandex.net translator API.
You must create an account at yandex.net to get the API KEY. The available languages are listed in their webpage, you should modify the **from_language** and **to_language** variables to change the languages. Make sure to modify the Python encoding to avoid problems with special characters, such as non latin alphabets.

### csgo price checker

Bot that will get the prices of csgo skins.
First of all you have to create an account at [CSGOLYZER](http://csgolyzer.com/) and download the item list from [CSGOLYZER item list](http://csgolyzer.com/api/items?api_key={your_api_key}) and save them at a file called *item* (NOTE: no extension).
One this is done, you should run the *csgo_load.py* which will generate a *weapons.txt* file from the item list.

Run the *csgo.py* script to start the bot! Remember it should only be used in inline mode, unless you can remember the exact same hash_name of every weapon.
