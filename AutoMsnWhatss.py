import pyautogui
from time import sleep
import pyperclip
#from datetime import datetime


def msn(msn, win):
    pyautogui.click(x=685, y=341)
    sleep(2)
    while True:
        win = 'N'  # str(input('A janela esta aberta? [S/N]').upper().title()[0])
        if win in "SN":
            break
    #while True:
        #hora = datetime.now()
        #hora = hora.strftime('%d/%m/%Y %H:%M')
        #if hora == '25/07/2022 23:56':
            #print(hora)
            #break

    if win == "N":
        pyautogui.PAUSE = .5
        sleep(2)
        pyautogui.click(x=488, y=745)
        pyautogui.write("Whatsapp")
        pyautogui.press('Enter')
        sleep(12)
    pyautogui.click(x=310, y=144)
    pyautogui.write('Grupo Teste')
    sleep(2)
    pyautogui.click(x=385, y=285)
    sleep(2)
    pyautogui.click(x=711, y=651)
    pyperclip.copy(msn)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    #--------------------------------------------
    pyautogui.click(x=310, y=144)
    pyautogui.write('Ezilda Rosa')
    sleep(2)
    pyautogui.click(x=385, y=285)
    sleep(2)
    pyautogui.click(x=711, y=651)
    pyperclip.copy(msn)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    #---------------------------------------------
    pyautogui.click(x=310, y=144)
    pyautogui.write('Rose Santos')
    sleep(2)
    pyautogui.click(x=385, y=285)
    sleep(2)
    pyautogui.click(x=711, y=651)
    pyperclip.copy(msn)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    #---------------------------------------------
    pyautogui.click(x=310, y=144)
    pyautogui.write('Mauricio Passos')
    sleep(2)
    pyautogui.click(x=385, y=285)
    sleep(2)
    pyautogui.click(x=711, y=651)
    pyperclip.copy(msn)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    #---------------------------------------------
    pyautogui.click(x=310, y=144)
    pyautogui.write('Andreia As')
    sleep(2)
    pyautogui.click(x=385, y=285)
    sleep(2)
    pyautogui.click(x=711, y=651)
    pyperclip.copy(msn)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')


msn(msn='''Bom dia...Tudo bem por aí? Tenha um ótimo dia. Bjs''', win='')
#str(input('Mensagem: ').capitalize()), win = '')
