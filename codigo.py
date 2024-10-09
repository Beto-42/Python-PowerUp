# Passo 1: Acessar o link do sistema - https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

#pyautogui.write - > Escrever um texto
#pyautogui.click  > Clicar com o mouse
#pyautogui.press  > apertar uma tecla
#pyautogui.hotkey > apertar um atalho de teclado (Ctrl, C)

pyautogui.PAUSE = 0.5

# abrir o navegador
# apertar a tecla win

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


# entrar no link do sistema - https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Passo 2: Fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# quero dar uma pausa de 3 segundos
time.sleep(3)
pyautogui.click(x=438, y=374)
pyautogui.write("pythoniompressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha aqui")

pyautogui.press("tab")
pyautogui.click(x=671, y=537)

time.sleep(2)

# Passo 3: Importar a base da dados

import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)


# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim



            
    
