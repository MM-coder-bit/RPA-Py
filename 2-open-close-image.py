# -------------------------------------------------------#
# Para testar esse código básico, verifique a maneira    |
# que ficou a distribuição  das telas e arquivos, dentro |
# da pasta imagem/2-open-cloese-image.png, ou o          |
# video/2-open-close-image.mkv                           |
# -------------------------------------------------------#

import pyautogui as pyag
from pyautogui import click,doubleClick,moveTo
from time import sleep

# Indique ao code qual foto abrir
print("Aponte o mouse para a foto da tela\n Aguardando ....\n")
sleep(2)
foto = pyag.position()
print("Salvo a posição")

# Posição do close da janela
bt_fechar = (2933,90)

# Movimenta até a foto
moveTo(foto,duration=1)
sleep(2)
#duplo click na foto, e aparecerá na janela
doubleClick()
sleep(2)
# fechar a exibição da imagem
moveTo(bt_fechar,duration=0.5)
click()