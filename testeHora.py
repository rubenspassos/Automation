from datetime import datetime
while True:
    hora = datetime.now()
    hora = hora.strftime('%d/%m/%Y %H:%M')
    if hora == '25/07/2022 23:37':
        print(hora)
        break