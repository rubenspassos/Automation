import pyautogui as pt
from time import sleep
from datetime import datetime

while True:
    hora = datetime.now()
    hora = hora.strftime('%d/%m/%Y %H:%M')
    if hora == '01/08/2022 17:38':
        break


pt.PAUSE = 1
pt.click(x=704, y=1061)
pt.click(x=373, y=19)
pt.click(x=75, y=51)
sleep(5)
pt.click(x=1035, y=206)
sleep(2)
#pt.click(x=786, y=850) #azul
# pt.click(x=1097, y=850) #vermalho
pt.click(x=1600, y=836) # verde
sleep(2)
pt.click(x=1100, y=279) #alterar
sleep(1)
pt.click(x=1799, y=12)






