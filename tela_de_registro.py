def tela_registro():

    # importações
    import PySimpleGUI as sg
    import pyodbc
    from tela_de_confirmação import tela_de_confirmacao


# conexão com o banco de daos
    dados_conexao = ("Driver={SQL Server};"
                     "Server=DESKTOP-688NT47\MSSQLSERVER02;"
                     "Database=Clientes")

    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()


# layout to aplicativo
    layout = [
        [sg.Text('E-mail:', size=(9, 2)), sg.Input(key='email')],
        [sg.Text('Senha:', size=(9, 2)), sg.Input(
            key='senha', password_char='*')],
        [sg.Text('Confirmação de Senha:', size=(9, 2)),
         sg.Input(key='senha2', password_char='*')],
        [sg.Text(key='msg_final')],
        [sg.Button('Registrar'), sg.Button('Cancelar')],
    ]

    window = sg.Window('Tela de Registro', layout)


# funcionalidade do aplicativo
    while True:
        evento, valor = window.read()

        if evento == sg.WIN_CLOSED:
            break

        if evento == 'Cancelar':
            confirmacao = tela_de_confirmacao()

            if confirmacao == True:
                break

        if evento == 'Registrar':

            email = valor['email']
            email = email.strip()
            email = email.replace(' ', '')
            senha = valor['senha']
            senha = senha.strip()
            senha = senha.replace(' ', '')
            senha2 = valor['senha2']
            senha2 = senha2.strip()
            senha2 = senha2.replace(' ', '')

            if senha == senha2:

                cursor.execute(
                    'select count(*) from Clientes.dbo.pessoas where email = ?', email)
                resultado = cursor.fetchone()
                resultado = resultado[0]

                if resultado > 0:
                    window['msg_final'].update('E-mail já registrado.')

                else:
                    cursor.execute(
                        'insert into Clientes.dbo.pessoas values (?, ?)', email, senha)
                    conexao.commit()
                    window['msg_final'].update(
                        'Usuário registrado com sucesso')

            else:
                window['msg_final'].update('Senhas não correspondem')

    window.close()
