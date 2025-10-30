from instagrapi import Client
import os

cl = Client()

USERNAME = os.getenv("")
PASSWORD = os.getenv("")

cl.login(USERNAME, PASSWORD)

# Actions
cl.user_follow("aradhya.555")
cl.direct_send("Hello from instagrapi!", ["aradhya.555"])



