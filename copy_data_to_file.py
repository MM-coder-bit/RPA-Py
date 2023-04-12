# ------------------------------------------------------------------- #
# Para testar esse código básico, verifique a maneira                 |
# que ficou a distribuição  das telas e arquivos, dentro              |
# da pasta imagem/Tela de teste.png, ou o video/Demonstracao-copy.mkv |
# ------------------------------------------------------------------- #

import pyautogui
from time import sleep

# captura a posição do mouse atual
print(pyautogui.position())

# Seleciona a data do arquivo RPA.txt
pyautogui.moveTo(2122,260)
sleep(0.5)
pyautogui.click()
pyautogui.dragTo(2251,260,1)

# Copia a data do arquivo RPA.txt
pyautogui.hotkey('ctrl','c')

# Cola no arquivo RPA_moved
pyautogui.moveTo(2737,168)
sleep(0.5)
pyautogui.click()
pyautogui.hotkey('ctrl','v')
