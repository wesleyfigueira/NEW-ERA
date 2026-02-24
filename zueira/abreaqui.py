import pyautogui
import time


messagem= "Você é Gay !!!"

pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('bloco de notas')  
pyautogui.press('enter')   
time.sleep(3)
pyautogui.write(messagem)
