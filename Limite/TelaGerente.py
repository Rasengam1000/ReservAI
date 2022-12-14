import PySimpleGUI as sg


class TelaGerente():
    def __init__(self):
        self.menu_cadastrar_func()

    @property
    def window_menu(self):
        return self.__window_menu

    def menu(self, cores, data="00/00/00"):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('MENU', font=("Arial", 20)), sg.Button("Sair", key="deslogar", pad=((640, 0),(10,0)))],
            [sg.Button('Menu Funcionário', key="menu_funcionario"), sg.Button('Menu Hóspede', key="menu_hospede"), sg.Button('Menu barco', key="menu_barco")],
            [sg.Button('Listar Reservas', key="listar_reservas"), sg.Button('Relatórios', key="relatorio")],

            [sg.Button("Dia anterior", key="se", pad=((0, 15), (30, 0))), sg.Text(f"{data}", font=("Arial", 13), key="data", pad=((0, 0), (30, 0))),sg.Button("Próximo dia", key="sd", pad=((15, 0), (30, 0)))],

            [sg.Button('QUARTO 1', key=1, pad=((0, 30),(70,0))), sg.Button('QUARTO 2', key=2, pad=((0, 30),(70,0))), sg.Button('QUARTO 3', key=3, pad=((0, 30),(70,0))), sg.Button('QUARTO 4', key=4, pad=((0, 0),(70,0)))],
            [sg.Text("          ", key="c1", background_color=cores[0], pad=((0, 61),(0,0))), sg.Text("          ", key="c2", background_color=cores[1], pad=((0, 61),(0,0))), sg.Text("          ", key="c3", background_color=cores[2], pad=((0, 61),(0,0))), sg.Text("          ", key="c4", background_color=cores[3], pad=((0, 0),(0,0)))],
            [sg.Button('QUARTO 5', key=5, pad=((0, 30),(30,0))), sg.Button('QUARTO 6', key=6, pad=((0, 30),(30,0))), sg.Button('QUARTO 7', key=7, pad=((0, 30),(30,0))), sg.Button('QUARTO 8', key=8, pad=((0, 0),(30,0)))],
            [sg.Text("          ", key="c5", background_color=cores[4], pad=((0, 61),(0,0))), sg.Text("          ", key="c6", background_color=cores[5], pad=((0, 61),(0,0))), sg.Text("          ", key="c7", background_color=cores[6], pad=((0, 61),(0,0))), sg.Text("          ", key="c8", background_color=cores[7], pad=((0, 0),(0,0)))], 
                ]
        self.__window_menu = sg.Window('MENU', size=(800, 450), element_justification="c").Layout(layout)

    def menu_funcionario(self):
        layout = [
            [sg.Text('Menu Funcionário', font=("Arial", 20))],

            [sg.Button('Cadastrar', key="cadastrar_funcionario")],
            [sg.Button('Alterar Informações', key="alterar_funcionario")],
            [sg.Button('Excluir', key="excluir_funcionario")],

            [sg.Button('Voltar', key=0)]
        ]
        self.__window_menu_funcionario = sg.Window('Menu Funcionário',  element_justification="c").Layout(layout)
    
    def menu_busca_funcionario(self):
        layout = [
            [sg.Text('Buscar Funcionário', font=("Arial", 15))],
            [sg.Text('CPF'), sg.Input(key="cpf")],

            [sg.Button('Buscar', key="buscar")],
            [sg.Button('Cancelar', key=0)]
        ]

        self.__window_busca_funcionario = sg.Window('Buscar Funcionário').Layout(layout)

    def menu_cadastrar_func(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [  
            [sg.Text('Cadastro Funcionário', font=("Arial", 15))],
            [sg.Text('Nome'), sg.Input(key="nome")],
            [sg.Text('Usuário'), sg.Input(key="usuario")],
            [sg.Text('Senha'), sg.Input(key="senha")],
            [sg.Text('CPF'), sg.Input(key="cpf")],
            [sg.Text('Data de Nascimento'), sg.Input(key="data_nascimento")],
            [sg.Text('Telefone'), sg.Input(key="telefone")],
            [sg.Text('E-mail'), sg.Input(key="email")],
            [sg.Button('Cadastrar', key="cadastrar")],
            [sg.Button('Cancelar', key=0)]
        ]

        self.__window_cadastro_func = sg.Window('Cadastro Funcionário').Layout(layout)

    def menu_alterar_funcionario(self, funcionario, senha):
        layout = [  
            [sg.Text('Alterar Funcionário', font=("Arial", 15))],
            [sg.Text('Nome'), sg.Text(funcionario.nome)],
            [sg.Text('Usuário'), sg.Input(funcionario.usuario, key="usuario")],
            [sg.Text('Senha'), sg.Input(senha, key="senha")],
            [sg.Text('CPF'), sg.Text(funcionario.cpf)],
            [sg.Text('Data de Nascimento'), sg.Text(funcionario.data_nascimento)],
            [sg.Text('Telefone'), sg.Input(funcionario.telefone, key="telefone")],
            [sg.Text('E-mail'), sg.Input(funcionario.email, key="email")],
            [sg.Button('Alterar', key="alterar")],
            [sg.Button('Sair', key=0)]
        ]
        self.__window_alterar_funcionario = sg.Window('Alterar Funcionário').Layout(layout)

    def menu_excluir_funcionario(self, nome_funcionario=None):
        confirmar = [
            [sg.Text('Tem certeza que deseja excluir:', font=("Arial", 15))],
            [sg.Text(nome_funcionario, font=("Arial", 15))],

            [sg.Button('Sim', key="sim")],
            [sg.Button('Cancelar', key=0)]
        ]
        
        self.__window_excluir_funcionario = sg.Window('Excluir Hóspede').Layout(confirmar)

    def opçoes_funcionario(self):
        self.menu_funcionario()
        button, values = self.__window_menu_funcionario.Read()
        if button is None:
            button = 0
        return button, values

    def buscar_funcionario(self):
        self.menu_busca_funcionario()
        button, values = self.__window_busca_funcionario.Read()
        if button is None:
            button = 0
        return button, values

    def cadastrar_funcionario(self):
        self.menu_cadastrar_func()
        while True:
            button, values = self.__window_cadastro_func.Read()
            
            vazio = False

            if button == None or button == 0 or button == sg.WIN_CLOSED:
                return button, values

            for valor in values.values():
                if valor == "" or valor == None:
                    vazio = True

            if vazio == True or not values["cpf"].isnumeric():
                self.msg("Todos os campos devem ser preenchidos!")
                continue
                
            return button, values

    def alterar_funcionario(self, funcionario, senha):
        self.menu_alterar_funcionario(funcionario, senha)
        while True:
            button, values = self.__window_alterar_funcionario.Read()
            
            vazio = False

            if button == None or button == 0 or button == sg.WIN_CLOSED:
                return button, values

            for valor in values.values():
                if valor == "" or valor == None:
                    vazio = True
                    break

            if vazio == True:
                self.msg("Todos os campos devem ser preenchidos corretamente!")
                continue
                
            return button, values

    def excluir_funcionario(self, nome_funcionario):
        self.menu_excluir_funcionario(nome_funcionario)
        button, values = self.__window_excluir_funcionario.Read()
            
        return button, values

    def opçoes_menu(self, data, cores, refresh=False):
        if refresh == False:
            self.menu(cores, data)

        button, values = self.__window_menu.Read()
        if button is None:
            button = 0
        return button, values

    def close_menu(self):
        self.__window_menu.Close()
        
    def close_opçoes_funcionario(self):
        self.__window_menu_funcionario.Close()

    def close_busca_funcionarios(self):
        self.__window_busca_funcionario.Close()

    def close_cadastrar_funcionario(self):
        self.__window_cadastro_func.Close()

    def close_alterar_funcionario(self):
        self.__window_alterar_funcionario.Close()

    def close_excluir_funcionario(self):
        self.__window_excluir_funcionario.Close()

    def msg(self, msg):
        sg.Popup(msg)
