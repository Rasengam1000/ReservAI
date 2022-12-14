import PySimpleGUI as sg


class TelaReserva():
    def __init__(self):
        pass

    def menu_reservar(self, quarto, dia):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Digite o CPF do Hóspede principal: ', font=("Arial", 15)), sg.Input(key="cpf")],
            [sg.Text(f"Quarto {quarto}", font=("Arial", 15))],
            [sg.Text('Data de Entrada: '), sg.Input(dia, key='data_entrada',size=(20,1)), sg.CalendarButton('Abrir Calendário', title='Selecione a data de entrada', no_titlebar=False, format='%d-%m-%y', close_when_date_chosen=False, target='data_entrada', month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('S', 'T', 'Q', 'Q', 'S', 'S', 'D'))],
            [sg.Text('Data de Saída: '), sg.Input(key='data_saida', size=(20,1)), sg.CalendarButton('Abrir Calendário', title='Selecione a data de saída', no_titlebar=False, format='%d-%m-%y', close_when_date_chosen=False, target='data_saida', month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('S', 'T', 'Q', 'Q', 'S', 'S', 'D'))],
            
            [sg.Button('Confirmar', key="reservar")],
            [sg.Button('Cancelar', key=0)]
        ]
        self.__windows_menu_reservar = sg.Window('MENU RESERVAR', size=(800, 450), element_justification="c").Layout(layout)

    def menu_reserva_hoje_reservado(self, reserva):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text(f'Reserva número: {reserva.cod} ', font=("Arial", 15))],
            [sg.Text(f'Hóspede principal: {reserva.lista_hospedes[0].nome} ({reserva.lista_hospedes[0].cpf}) ', font=("Arial", 15))],
            [sg.Text(f'Data de Entrada: {reserva.data_entrada}')],
            [sg.Text(f'Data de Saída: {reserva.data_saida}')],
            
            [sg.Button('Check-in', key="check-in"), sg.Button('Excluir Reserva', key="excluir")],
            [sg.Button('Voltar', key=0)]
        ]
        self.__windows_menu_reserva_hoje_reservado = sg.Window('MENU RESERVA', size=(800, 450), element_justification="c").Layout(layout)

    def menu_reserva_hoje_ocupado(self, reserva):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text(f'Reserva número: {reserva.cod} ', font=("Arial", 15))],
            [sg.Text(f'Hóspede principal: {reserva.lista_hospedes[0].nome} ({reserva.lista_hospedes[0].cpf}) ', font=("Arial", 15))],
            [sg.Text(f'Data de Entrada: {reserva.data_entrada}')],
            [sg.Text(f'Data de Saída: {reserva.data_saida}')],
            
            [sg.Button('Finalizar Reserva (checkout)', key="check-out")],
            [sg.Button('Voltar', key=0)]
        ]
        self.__windows_menu_reserva_hoje_ocupado = sg.Window('MENU RESERVA', size=(800, 450), element_justification="c").Layout(layout)

    def menu_reserva_outro_reservado(self, reserva):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text(f'Reserva número: {reserva.cod} ', font=("Arial", 15))],
            [sg.Text(f'Hóspede principal: {reserva.lista_hospedes[0].nome} ({reserva.lista_hospedes[0].cpf}) ', font=("Arial", 15))],
            [sg.Text(f'Data de Entrada: {reserva.data_entrada}')],
            [sg.Text(f'Data de Saída: {reserva.data_saida}')],
            
            [sg.Button('Excluir Reserva', key="excluir")],
            [sg.Button('Voltar', key=0)]
        ]
        self.__windows_menu_reserva_outro_reservado = sg.Window('MENU RESERVA', size=(800, 450), element_justification="c").Layout(layout)

    def menu_reserva_outro_ocupado(self, reserva):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text(f'Reserva número: {reserva.cod} ', font=("Arial", 15))],
            [sg.Text(f'Hóspede principal: {reserva.lista_hospedes[0].nome} ({reserva.lista_hospedes[0].cpf}) ', font=("Arial", 15))],
            [sg.Text(f'Data de Entrada: {reserva.data_entrada}')],
            [sg.Text(f'Data de Saída: {reserva.data_saida}')],
            
            [sg.Button('Voltar', key=0)]
        ]
        self.__windows_menu_reserva_outro_ocupado = sg.Window('MENU RESERVA', size=(800, 450), element_justification="c").Layout(layout)
    
    def menu_lista_reservas(self, lista, cores):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('RESERVAS DO DIA', font=("Arial", 20))],
            [sg.Table(values=lista,  key="playlist",
                         num_rows=17,
                         headings=["Quarto", "Status", "Código", "Data Entrada", "Data Saída", "Hóspede"],
                         row_colors=cores,
                         justification="c",
                         pad=((0, 0), (20, 0))
                         )
            ],
            [sg.Button("Voltar", key=0, pad=((0, 0), (20, 0)))]
                ]
        self.__window_menu_lista_reservas = sg.Window('RESERVAS', size=(800, 450), element_justification="c").Layout(layout)

    def menu_cancelar(self, multa=None):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text("Deseja mesmo excluir esta reserva?")],      
            [sg.Button('Sim', key=1), sg.Button('Não', key=0)]
        ]
        layout_multa = [
            [sg.Text(f"O período de cancelamento passou.\nMulta: {multa} reais.")],      
            [sg.Button('Confirmar Pagamento', key=1)]
        ]
        self.__window_cancelar = sg.Window('EXCLUIR', element_justification="c").Layout(layout)
        self.__window_cancelar_multa = sg.Window('EXCLUIR', element_justification="c").Layout(layout_multa)

    def abrir_tela_check_in(self, reserva, hospedes):
        #TODO PEGAR DADOS DE QUARTO E ETC
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text(
                f"Check-in no quarto {reserva.quarto.numero} - capacidade para {reserva.quarto.capacidade} pessoas.")]]
        for i in range(len(hospedes)):
            layout.append([sg.Text(f"Hóspede {i+1}: {hospedes[i].nome}({hospedes[i].cpf})")])
        if len(hospedes) < reserva.quarto.capacidade:
            layout.append([sg.Text(f"Adicionar outro, inserir CPF:"), sg.Input(key="cpf"),  sg.Button('+', key="add_hospede")])
        layout.append([sg.Button('Confirmar', key="check-in")])
        layout.append([sg.Button('Cancelar', key=0)])

        self.__windows_menu_check_in = sg.Window('MENU CHECK-IN', size=(800, 450), element_justification="c").Layout(
            layout)

    def opçoes_menu_lista_reservas(self, lista, cores):
        self.menu_lista_reservas(lista, cores)

        button, values = self.__window_menu_lista_reservas.Read()
        if button is None:
            button = 0
        return button, values

    def opçoes_menu_reserva_hoje_reservado(self, reserva):
        self.menu_reserva_hoje_reservado(reserva)
            
        button, values = self.__windows_menu_reserva_hoje_reservado.Read()

        if button == None or button == 0 or button == sg.WIN_CLOSED:
            return button, values

        return button, values

    def menu_check_in(self, reserva, hospedes):
        self.abrir_tela_check_in(reserva, hospedes)
        while True:

            button, values = self.__windows_menu_check_in.Read()

            vazio = False

            if button == None or button == 0 or button == sg.WIN_CLOSED:
                return button, values

            for valor in values.values():
                if valor == "" or valor == None:
                    vazio = True
                    break
            if button == "add_hospede":
                if vazio == True or not values["cpf"].isnumeric():
                    self.msg("Todos os campos devem ser preenchidos corretamente!")
                    continue

            return button, values

    def opçoes_menu_reserva_hoje_ocupado(self, reserva):
        self.menu_reserva_hoje_ocupado(reserva)
            
        button, values = self.__windows_menu_reserva_hoje_ocupado.Read()

        if button == None or button == 0 or button == sg.WIN_CLOSED:
            return button, values

        return button, values
    
    def opçoes_menu_reserva_outro_reservado(self, reserva):
        self.menu_reserva_outro_reservado(reserva)
            
        button, values = self.__windows_menu_reserva_outro_reservado.Read()

        if button == None or button == 0 or button == sg.WIN_CLOSED:
            return button, values

        return button, values
    
    def opçoes_menu_reserva_outro_ocupado(self, reserva):
        self.menu_reserva_outro_ocupado(reserva)
            
        button, values = self.__windows_menu_reserva_outro_ocupado.Read()

        if button == None or button == 0 or button == sg.WIN_CLOSED:
            return button, values

        return button, values

    def opçoes_reservar(self, quarto, dia, retomar=False):
        if retomar == False:
            self.menu_reservar(quarto, dia)
        while True:
            button, values = self.__windows_menu_reservar.Read()

            if button == None or button == 0 or button == sg.WIN_CLOSED:
                return button, values

            values.pop("Abrir Calendário")      #tirar o campo do calendario q é inutil (e sao 2)
            values.pop("Abrir Calendário0")

            vazio = False

            for valor in values.values():
                if valor == "" or valor == None:
                    vazio = True
                    break

            if not values["cpf"].isnumeric():
                self.msg("O CPF deve ser digitado apenas com números")
                continue

            if vazio == True:
                self.msg("Todos os campos devem ser preenchidos!")
                continue

            data1 = values["data_entrada"].split("-")
            data2 = values["data_saida"].split("-")
            
            if any([len(x) != 2 or len(data1) != 3 for x in data1]) or any([len(x) != 2 or len(data2) != 3 for x in data2]):
                self.msg("O formato da data deve ser Ex: '29-12-22'")
                continue

            return button, values

    def opçao_cancelar(self, multa=None):
        self.menu_cancelar(multa)
        if multa != None:
            opçao, valores = self.__window_cancelar_multa.Read()
            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                return opçao, valores

        opçao, valores = self.__window_cancelar.Read()
        self.__window_cancelar.close()
        self.__window_cancelar_multa.close()

        return opçao, valores
        
        
    def close_menu_reservar(self):
        self.__windows_menu_reservar.Close()

    def close_menu_lista_reservas(self):
        self.__window_menu_lista_reservas.Close()
        
    def close_menu_reserva_hoje_reservado(self):
        self.__windows_menu_reserva_hoje_reservado.Close()

    def abrir_tela_check_out(self, reserva, valor):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text(f"Check-out do quarto {reserva.quarto.numero}")],
            [sg.Text(f"O valor total da reserva foi R${valor}")]]
        layout.append([sg.Button('Confirmar pagamento', key="check-out")])
        layout.append([sg.Button('Cancelar', key=0)])

        self.__windows_menu_check_out = sg.Window('MENU CHECK-OUT', size=(800, 450), element_justification="c").Layout(
            layout)

    def menu_check_out(self, reserva, valor):
        
        self.abrir_tela_check_out(reserva, valor)
        button, values = self.__windows_menu_check_out.Read()

        if button == None or button == 0 or button == sg.WIN_CLOSED:
            return button, values

        return button, values

    def close_menu_reserva_hoje_ocupado(self):
        self.__windows_menu_reserva_hoje_ocupado.Close()

    def close_menu_check_in(self):
        self.__windows_menu_check_in.Close()

    def close_menu_check_out(self):
        self.__windows_menu_check_out.Close()

    def close_menu_reserva_outro_reservado(self):
        self.__windows_menu_reserva_outro_reservado.Close()

    def close_menu_reserva_outro_ocupado(self):
        self.__windows_menu_reserva_outro_ocupado.Close()

    def msg(self, msg):
        sg.Popup(msg)