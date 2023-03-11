from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import urlretrieve
import time
import pprint
import keyboard
from io import BytesIO
import win32clipboard
from PIL import Image
import os


if os.path.exists("sample_data"):
    pass
else:
    os.mkdir("sample_data")

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


no_of_pics = 10
time.sleep(5)

options = Options()
options.headless = True
options.add_argument('log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

driver.get('https://www.google.com/search?q=want+to+talk+with+you+pics+cute&rlz=1C1GCEB_enIN978IN978&hl=en&sxsrf=AJOqlzUbARKVRw9fnyO7ScfvRDX5FVKXlA:1678438865941&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjcvoaDgNH9AhUn9DgGHeFmCycQ_AUoAXoECAIQAw')

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)

imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'Q4LuWd')]")


src = []
for img in imgResults:
    src.append(img.get_attribute('src'))

for i in range(no_of_pics):
    urlretrieve(str(src[i]),"sample_data/pets{}.jpg".format(i))

#------------------------------web_scrapping section---------------------------

for i in range(no_of_pics):
    filepath = 'sample_data/pets{}.jpg'.format(i)
    image = Image.open(filepath)

    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    send_to_clipboard(win32clipboard.CF_DIB, data)
    keyboard.press_and_release('ctrl + v')
    time.sleep(0.5)
    keyboard.press_and_release('enter')
    time.sleep(10)
#------------------------------keyboard pic section----------------------------
for i in range(no_of_pics):
    filepath = 'sample_data/pets{}.jpg'.format(i)
    os.remove(filepath)
#---------------------------------remove section-----------------------------
