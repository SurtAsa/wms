# importando bibliotecas
import pyautogui as pg
import webbrowser as web
import time
import pandas as pd

# importando csv
contatos = pd.read_csv("Lista_Contato_Whatapp.csv")

# fazendo o envio
data_dict = contatos.to_dict('list')

leads = data_dict['wpp']
messages = data_dict['msg']
combo = zip(leads,messages)
first = True
for lead,messages in combo:
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+messages)
    if first:
        time.sleep(4)
        first=False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(5)
    pg.press('esc')
    time.sleep(3)
    pg.press('enter')
    time.sleep(4)
    pg.hotkey('ctrl','w')