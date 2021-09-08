from pyrogram import Client

api_id = 
api_hash = ""

with Client("my_account", api_id, api_hash) as app:
    app.send_message("me", "Greetings from **Pyrogram**!")
