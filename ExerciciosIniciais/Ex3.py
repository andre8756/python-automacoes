import pyautogui
import time


# Clicar na aba certa 
pyautogui.moveTo(x=500, y=1050)
time.sleep(1)

pyautogui.click()
time.sleep(2)

pyautogui.moveTo(x=900, y=980)
time.sleep(1)

pyautogui.click()
time.sleep(2)

pyautogui.write("testes")
time.sleep(2)

pyautogui.press("enter")
