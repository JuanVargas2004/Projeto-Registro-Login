def tela_login():

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
        [sg.Text('E-mail:')],
        [sg.Input(key='email')],
        [sg.Text('Senha:')],
        [sg.Input(key='senha', password_char='*')],
        [sg.Text(key='msg_final')],
        [sg.Button('Login'), sg.Button('Cancelar')],
    ]

    window = sg.Window('Tela de Login', layout)


# funcionalidade do aplicativo
    while True:
        evento, valor = window.read()

        if evento == sg.WIN_CLOSED:
            break

        if evento == 'Cancelar':

            confirmacao = tela_de_confirmacao()

            if confirmacao == True:
                break

        if evento == 'Login':

            email = valor['email']
            email = email.strip()
            email = email.replace(' ', '')
            senha = valor['senha']
            senha = senha.strip()
            senha = senha.replace(' ', '')

            cursor.execute(
                'select count(*) from Clientes.dbo.pessoas where email = ?', email)
            resultado = cursor.fetchone()

            if resultado[0] > 0:

                cursor.execute(
                    'select email, senha from Clientes.dbo.pessoas where email = ?', email)
                resultado = cursor.fetchone()
                resultado_email = resultado[0]
                resultado_senha = resultado[1]

                if resultado_email == email and resultado_senha == senha:
                    window['msg_final'].update('Bem Vindo')

                else:
                    window['msg_final'].update('Credenciais inválidas')

            else:
                window['msg_final'].update('Credenciais inválidas')

    window.close()
