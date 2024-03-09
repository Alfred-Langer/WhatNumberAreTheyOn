import webbrowser
import time
import os
from dotenv import load_dotenv

load_dotenv()
url = os.environ['UDC_URL']
edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
webbrowser.get((edge_path)).open(url)
time.sleep(10)