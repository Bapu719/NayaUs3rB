
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Ya need to go my.telegram.org
and login using your ph 
Apply for Api dev 
and get the details mentioned below""")
APP_ID = int(input(" APP ID here: "))
API_HASH = input(" API HASH here: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
