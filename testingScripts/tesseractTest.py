from plistlib import load
import cv2
import pytesseract
import pyautogui
from dotenv import load_dotenv

load_dotenv()
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'



#pyautogui.screenshot("screenshotTesting.png",region=(1150,50,750,116))

img = cv2.imread("currentScreenshot.png")
text = pytesseract.image_to_string(img)
print(text)