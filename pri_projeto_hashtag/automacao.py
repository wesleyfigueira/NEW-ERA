import pyautogui
import time


link ='https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

time.sleep(5)

pyautogui.write(link)
time.sleep(1)
pyautogui.press('enter')

time.sleep(5)

pyautogui.click(x=447, y=628, clicks=2) 
time.sleep(3)

pyautogui.click(x=610, y=625)
time.sleep(3)
pyautogui.click(x=713, y=201)