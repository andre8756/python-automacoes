import pyautogui
import time

pyautogui.hotkey('win', 'r')
time.sleep(2)
pyautogui.write('cmd')
pyautogui.press('enter')
time.sleep(3)

pyautogui.write("taskkill /f /im cmd.exe /t")
pyautogui.press("enter")