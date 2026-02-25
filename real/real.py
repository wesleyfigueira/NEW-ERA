import pyautogui
import time


pyautogui.PAUSE = 1

grievance=('https://churchofjesuschrist.sharepoint.com/:x:/r/sites/StudentWellness/_layouts/15/Doc.aspx?sourcedoc=%7B5F873C45-0B39-4930-945F-6395F6A655F6%7D&file=CASES%202025.xlsx&action=default&mobileredirect=true')
email =('https://outlook.office.com/mail/inbox/id/AAQkADEyZmRjMjBlLTc1YjUtNDFlNy1iNTM1LWVmYTBiY2ZiOTJlYQAQALCDscd0EH9PihEgW6Th4u8%3D')

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(5)

pyautogui.click(x=1288, y=709, clicks=2)
time.sleep(2)

pyautogui.write(email)
pyautogui.press('enter')
time.sleep(5 )

pyautogui.click(x=2287, y=20)

pyautogui.write(grievance)
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=2588, y=24)
pyautogui.write('https://youtu.be/UAFCCqmMUuY?list=RDUAFCCqmMUuY')
pyautogui.press('enter')