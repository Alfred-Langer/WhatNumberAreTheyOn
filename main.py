import webbrowser
import os
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv
import pyautogui
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import re
import time
import cv2

class potentialNextNumber:
    def __init__(self, number, counter):
        self.number = number
        self.counter = counter

def validateText(inputText):
    validCharacters = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'"
    if len(inputText) < 3:
        return False

    inputTextIndex = re.search(r"\d", inputText)
    if inputTextIndex:
        inputText = inputText[inputTextIndex.start():]
        newText = [c for c in inputText[:3] if c in validCharacters]
        if not ''.join(newText).isdigit():
            return False
        newText.extend(c for c in inputText[3:] if c in validCharacters)
        return ''.join(newText)
    else:
        return False    

def is_in_range(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound

lastRecordedNumber = -1
maybeNextNum = None
time.sleep(10)

if __name__ == "__main__":
    #Load Environment variables from the .env file
    load_dotenv()
    

    #Create the Webhook to communicate with the Discord Server
    #webhook = DiscordWebhook(url=os.environ['DISCORD_WEBHOOK'],content="Testing")
    #response = webhook.execute()


    while(True):
        pyautogui.screenshot("screenshot.png",region=(960,14,951,46))
        #pyautogui.screenshot("screenshot.png",region=(350,950,1070,85))
        img = cv2.imread("screenshot.png")
        text = pytesseract.image_to_string(img)
        print(text)
        validatedText = validateText(text)

        
        if validatedText:
            validatedNumber = int(validatedText[:3])
            if lastRecordedNumber != validatedNumber and (lastRecordedNumber == -1):
                if(maybeNextNum == None or maybeNextNum.number != validatedNumber):
                    maybeNextNum = potentialNextNumber(validatedNumber, 1)
                elif (maybeNextNum.number == validatedNumber):
                    maybeNextNum.counter += 1
                    if maybeNextNum.counter >= 5:
                        lastRecordedNumber = validatedNumber
                        webhook = DiscordWebhook(url=os.environ['DISCORD_WEBHOOK_URL'],content=str(validatedNumber))
                        response = webhook.execute()
                        print("NUMBER IS: " + str(validatedNumber))
                        currentNumber = validatedNumber
                        maybeNextNum = None

            elif lastRecordedNumber == validatedNumber:
                print("Currently on the same number")
            else:
                print("Number is not in range of last recorded number, assuming that pytesseract read the wrong number")
        else:
            print("Can't find number in string")

        time.sleep(0.5)