import PySimpleGUI as sg


class TelaBarco:
    def __init__(self):
        self.menu_barcos()

    def menu_barcos(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Digite o número da reserva: ', font=("Arial", 15)), sg.Input(key="n_reserva")],
            [sg.Text('Digite o número do barco (teste) 1, 2, 3: ', font=("Arial", 15)), sg.Input(key="n_barco")],
            [sg.Text('Data de Entrada: '), sg.Input(key='data_entrada', size=(20,1)), sg.CalendarButton('Abrir Calendário', title='Selecione a data de entrada', no_titlebar=False, format='%d-%m-%y', close_when_date_chosen=False, target='data_entrada', month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('S', 'T', 'Q', 'Q', 'S', 'S', 'D'))],
            
            [sg.Button('Confirmar', key=1)],
            [sg.Button('Cancelar', key=0)]
        ]
        self.__windows_menu_reserva = sg.Window('MENU RESERVA', size=(800, 450), element_justification="c").Layout(layout)

    def opçoes_reserva(self):
        self.menu_barcos()
        while True:
            button, values = self.__windows_menu_reserva.Read()
            print(values)
            values.pop("Abrir Calendário")      #tirar o campo do calendario q é inutil (e sao 2)

            vazio = False
            if button == None or button == 0 or button == sg.WIN_CLOSED:
                return button, values

            for valor in values.values():
                if valor == "" or valor == None:
                    print(valor)
                    vazio = True
                    break

            if not values["n_reserva"].isnumeric():
                self.msg("O número da reserva deve ser digitado apenas com números")
                continue

            if vazio == True:
                self.msg("Todos os campos devem ser preenchidos!")
                continue

            data1 = values["data_entrada"].split("-")
            print(data1)
            if any([len(x) != 2 or len(data1) != 3 for x in data1]):
                self.msg("O formato da data deve ser Ex: '29-12-22'")
                continue

            return button, values


    def close_menu_reserva(self):
        self.__windows_menu_reserva.Close()

    def msg(self, msg):
        sg.Popup(msg)