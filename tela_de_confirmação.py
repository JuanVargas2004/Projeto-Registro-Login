def tela_de_confirmacao():

    # importações
    import PySimpleGUI as sg


# layout to aplicativo
    layout = [
        [sg.Text('Você tem certeza que deseja cancelar essa operação?')],
        [sg.Button('Sim'), sg.Button('Não')],
    ]

    window = sg.Window('', layout)


# funcionalidade do aplicativo
    confirmacao = False
    while True:
        evento, valores = window.read()

        if evento == sg.WIN_CLOSED or evento == 'Não':
            break

        if evento == 'Sim':
            confirmacao = True
            break

    window.close()
    return confirmacao
