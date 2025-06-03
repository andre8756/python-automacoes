import pyautogui
import time


## Passo 1: Abrindo o navegador
#pyautogui.press("win")
#time.sleep(1)
#pyautogui.write("chrome")
#time.sleep(1)
#pyautogui.press("enter")
#time.sleep(3)

#-------------------
pyautogui.hotkey("win", "3")

# Digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=2445, y=475)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir para todos os produtos