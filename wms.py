# import libs
import pyautogui as pg
import webbrowser as web
import time
import pandas as pd

# import csv file
contatos = pd.read_csv("Lista_Contato_Whatapp.csv")

# send messages
data_dict = contatos.to_dict('list')

leads = data_dict['wpp']
messages = data_dict['msg']
send = data_dict['send']
value = data_dict['value']
description = data_dict['description']
pix = data_dict['pix']
combo = zip(leads,messages,send, value, description, pix)
first = True
def sender(first,lead,messages):
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+messages)
    if first:
        time.sleep(4)
        first = False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)
    pg.press('esc')
    time.sleep(5)
    pg.press('enter')
    time.sleep(5)
    pg.hotkey('ctrl','w')
for lead,messages,send, value, description, pix in combo:
    if send == "yes":
        messages = (f"Boa noite irmão! Como está por ai? Estou mandando os valores que ficaram pendentes para o mês de Outubro/22. Se preferir pagar por PIX a minha chave é: {pix} Se optar pelo pagamento via PIX, peço apenas que me mande o comprovante pelo privado. Valor: {value}. Descrição: {description}. Qualquer dúvida estou à disposição! V.S.S.V.")
        sender(first,lead,messages)
    elif send == "admin":
        sender(first,lead,messages)
