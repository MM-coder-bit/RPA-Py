import pyautogui

tamanho_tela = pyautogui.size()
print(f'Tamanho da tela: {tamanho_tela}')

position = pyautogui.position()
print(f'Posicao do mouse: {position}')

# --- Move para a posição absoluta ---- #
#pyautogui.moveTo(2,884)
pyautogui.moveTo(2,884,duration=1)