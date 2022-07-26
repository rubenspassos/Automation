import pyautogui
from time import sleep
import pyperclip

def msn(msn,win):
    while True:
        win = str(input('A janela esta aberta? [S/N]').upper().title()[0])
        if win in "SN":
            break
    if win == "N":
        pyautogui.PAUSE = 1
        sleep(2)
        pyautogui.click(x=488, y=745)
        pyautogui.write("Whatsapp")
        pyautogui.press('Enter')
        sleep(12)
    pyautogui.click(x=369, y=150)
    pyautogui.write('Grupo Teste')
    pyautogui.click(x=385, y=285)
    sleep(2)
    pyautogui.click(x=711, y=651)
    pyperclip.copy(msn)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

msn(msn = str(input('Mensagem: ').capitalize()), win = '')






