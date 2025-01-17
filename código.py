import pyautogui
import time
import pandas

pyautogui.PAUSE= 0.6

#acessar o sistema da empresa

#aperta a tecla windows
pyautogui.press("win")
#digitar o texto chrome
pyautogui.write("chrome")
#aperta a tecla enter
pyautogui.press("enter")
#acessa o sistema
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#comando para o computador esperar 3 segundos

time.sleep (3)

#fazer login no sistema.

pyautogui.click(x=700, y=407)
pyautogui.write("teste.teste@teste.com")

pyautogui.press("tab") #passa para o campo senha
pyautogui.write("coxinhas112")

pyautogui.press("tab") #passa para o botão "logar"
pyautogui.press("enter")

#importa a base de dados dos produtos

tabela = pandas.read_csv("produtos.csv")

print(tabela)

time.sleep(3)

#Cadastra os produtos

for linha in tabela.index:
    posicao = x=731, y=296
    pyautogui.click(posicao)

    #Código do produto
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #Marca
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #Tipo
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #Categoria
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #Preco_unitario
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #Custo
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #Obs
    obs = tabela.loc[linha,"obs"]
    if obs !="nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter") #apertar o bottão de enviar

    pyautogui.scroll(1000)
