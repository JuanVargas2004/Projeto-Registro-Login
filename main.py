import PySimpleGUI as sg
from tela_de_registro import tela_registro
from tela_de_login import tela_login


sg.theme('DarkGrey5')

layout = [
    [sg.Text('              Bem Vindo')],
    [sg.Button('Registro'), sg.Text('             ', key='espaço'),
     sg.Button('  Login  ', key='Login')],
]


window = sg.Window('', layout)

evento_registro = False
evento_login = False
while True:
    evento, _ = window.read()

    if evento == sg.WIN_CLOSED:
        break

    if evento == 'Registro':
        evento_registro = True
        break

    if evento == 'Login':
        evento_login = True
        break

window.close()


if evento_registro == True:
    tela_registro()


if evento_login == True:
    tela_login()
