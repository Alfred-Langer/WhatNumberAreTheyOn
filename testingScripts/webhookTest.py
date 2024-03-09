import os
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv
import pyautogui
import re


if __name__ == "__main__":
    #Load Environment variables from the .env file
    load_dotenv()

    #Create the Webhook to communicate with the Discord Server
    webhook = DiscordWebhook(url=os.environ['DISCORD_WEBHOOK_URL'],content="Testing")
    response = webhook.execute()