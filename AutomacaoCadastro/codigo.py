import pyautogui
import time
import pandas

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

time.sleep(3)

# Passo 3: Importar a base de dados - pandas
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar 1 produto

for linha in tabela.index:  
    pyautogui.click(x=2333, y=358)
    time.sleep(1)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))

    pyautogui.press("tab")
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))

    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))

    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    
    if obs != "nan":
        pyautogui.write(str(obs))
    

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)
    time.sleep(2)

# Passo 5: Repetir para todos os produtos