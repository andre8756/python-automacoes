import pyautogui
import time

# Abrir o windows
pyautogui.press("win")
time.sleep(3)

#Digitar "bloco de notas"
pyautogui.write("bloco de notas")
time.sleep(5)

# Abrir aplicativo
pyautogui.press("enter")
time.sleep(10)

#Digitar no bloco de notas
pyautogui.write("Hello World!!")