from Limite.TelaReserva import TelaReserva
from Entidade.ReservaQuarto import ReservaQuarto
from Entidade.Quarto import Quarto
from Persistencia.DAOquarto import DAOquarto   # temporario para testes
import PySimpleGUI as sg
from datetime import datetime as dt


class ControladorReserva:
    def __init__(self, controlador_sistema, controlador_hospede, dao_reserva):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_hospede = controlador_hospede

        self.__reserva_dao = dao_reserva
        self.__quarto_dao = DAOquarto()      # temporario para testes
        self.__tela_reserva = TelaReserva()
        self.criar_quartos()

    @property
    def reservas(self):
        return self.__reserva_dao.get_all()

    def criar_quartos(self):                                                        # temporario para teste
        if self.__quarto_dao.cache["quartos"] == []:                                
            for i in range(1,5):
                quarto = Quarto(i, 2, 1, 0, 500, "Quarto Casal (2 lugares)", 0)
                self.__quarto_dao.add(quarto)
            for i in range(5,9):
                quarto = Quarto(i, 4, 1, 2, 1000, "Quarto Familia (4 lugares)", 0)
                self.__quarto_dao.add(quarto)

    def alterar_status_res(self, reserva, status):
        pass

    def calcula_passeio(self, reserva):
        passeios = 0
        for reserva_barco in self.__reserva_barco_dao.get_all():
            if reserva_barco.cod_reserva == reserva:
                passeios += 1
        return passeios

    def calcula_diarias(self, reserva):  
        inicio = reserva.data_entrada
        fim = reserva.data_saida
        diarias = (dt.strptime(inicio, "%d/%m/%y") - dt.strptime(fim, "%d/%m/%y")).days
        print(f"A reserva durou {diarias} dias!")

        return diarias

    def calcular_valor(self, reserva):
        valor_diarias = self.calcula_diarias(reserva)*reserva.quarto.valor
        valor_barco = self.calcula_passeio(reserva.cod)
        valor_total = (valor_diarias) + (valor_barco)

        return valor_total
    

    #def checar_data_livre(self):
        # loop reservas / datas, data livre?

        # if data livre break / else voltar tela com preenchimento para alterar

    def realizar_reserva(self, n_quarto, dia):
        print(dia)
        opçao, valores = self.__tela_reserva.opçoes_reservar(n_quarto, dia)
        print(opçao,valores)
        
        if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
            self.__tela_reserva.close_menu_reservar()
            return

        # if self.checar_data_livre: data final apenas

        hospede = self.__controlador_hospede.buscar_hospede(valores["cpf"])

        if hospede:    # existe
            self.__tela_reserva.close_menu_reservar()
        else:     # nao existe
            hospede = self.__controlador_hospede.cadastrar()
            
        if hospede == None:
            return

        quarto = self.__quarto_dao.getQuarto(int(valores["n_quarto"]))

        cod = self.__reserva_dao.getCodUltimaReserva() + 1
        reserva = ReservaQuarto(cod, 1, quarto, [hospede], "10-07-22",                          # mesmo hospede com endereços de mem diferentes?
                                valores["data_entrada"], valores["data_saida"])
        self.__reserva_dao.add(reserva)

        self.__tela_reserva.msg("Reserva realizada com sucesso!")
        self.__tela_reserva.close_menu_reservar()

        for i in self.__reserva_dao.get_all():                              # mesmo quarto com endereços de mem diferentes?
            print(i.info_basica())                      
        return 1

    def editar_reserva(self, n_quarto):
        print("editar")
        pass

    def excluir_reserva(self, n_quarto):
        print("excluir")
        pass

    def getReservadoDia(self, n_quarto, dia):
        #hoje = dt.now()                     # dia de hoje, deixar alterar dps
        for reserva in self.reservas:
            if reserva.quarto.numero == n_quarto:
                inicio = reserva.data_entrada
                fim = reserva.data_saida
                if dt.strptime(inicio, "%d-%m-%y") <= dt.strptime(dia, "%d-%m-%y") < dt.strptime(fim, "%d-%m-%y"):
                    return reserva
        return 0
                
    def abre_tela(self, botao, dia):                 # clica quarto mapa (recebe numero dele aqui (botao))

        lista_opçoes = {"reservar": self.realizar_reserva, "editar": self.editar_reserva, "excluir": self.excluir_reserva,
                        "check-in": print("self.check-in"), "checkout": print("self.checkout")}
        
        while True:
            for i in self.__reserva_dao.get_all():                              # mesmo quarto com endereços de mem diferentes?
                print(i.quarto.numero, i.data_entrada, i.data_saida)   
            reserva = self.getReservadoDia(botao, dia)
            print(reserva)
            if reserva:
                if reserva.status == 1:
                    if dt.strptime(reserva.data_entrada, "%d-%m-%y") < dt.today() < dt.strptime(reserva.data_saida, "%d-%m-%y"):
                        opçao, valores = self.__tela_reserva.opçoes_menu_reserva_hoje_reservado(reserva)
                        self.__tela_reserva.close_menu_reserva_hoje_reservado()
                    else:
                        opçao, valores = self.__tela_reserva.opçoes_menu_reserva_outro_reservado(reserva)
                        self.__tela_reserva.close_menu_reserva_outro_reservado()
                elif reserva.status == 2:
                    opçao, valores = self.__tela_reserva.opçoes_menu_reserva_hoje_ocupada(reserva)
                    self.__tela_reserva.close_menu_reserva_hoje_ocupado()

                if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                    break

                if opçao in ["editar", "excluir"]:      # e checkin checkout (finalizar)
                    lista_opçoes[opçao](botao)

            else:

                self.realizar_reserva(botao, dia)
                break


