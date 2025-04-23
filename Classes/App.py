from Functions.Inputs import *
from Functions.Tables import today
from Functions.Prints import *
from Classes.Excel import Excel

class App:
    def __init__(self):
        self.APP_NAME = "Rent Manager | J&S - Administração de Imóveis"
        self.VERSION = "0.0.1"
        self.OPTIONS = ["Encontrar alugueis vencidos","Alterar base de dados", "Registros", "Informações", "Sair do Aplicativo"]

    def run(self):
        clear()
        wait(1)
        print(f"{self.APP_NAME} | J&S - Administração de Imóveis")
        print("Bem-vindo")
        wait(2)
        
        while True:
            clear()

            function = choose_options(self.OPTIONS)
            clear()
            if function == 0 :
                self.find_menu()

            if function == 1:
                self.modify_table_menu()
                
            if function == 2 :
                excel = Excel()
                excel.show_data()

            if function == 3 :
                print(self)
                
            if function == len(self.OPTIONS)-1:
                return

            input("Pressione qualquer tecla para prosseguir")
            clear()

    def find_menu(self):
        OPTIONS = ["Encontrar alugueis vencidos hoje", "Encontrar alugueis vencidos em data específica", "Voltar"]

        function = choose_options(OPTIONS)
        if function == 0:
            excel = Excel()
            data = excel.get_overdue_rents(today())

            if len(data) == 0:
                print("Não há imóveis a serem cobrados hoje")
            else:
                print_apartments(data)
            
        if function == 1:
            excel = Excel()

            while True:
                date = input_integer("Digite o dia do vencimento:")
                if date >= 1 or date <= 31:
                    break
                print("O valor inserido não é válido")

            date = int(date)
            data = excel.get_overdue_rents(date)

            if len(data) == 0:
                print(f"Não há imóveis a serem cobrados no dia {date}")
            else:
                print_apartments(data)

        if function == len(OPTIONS)-1:
            return

    def modify_table_menu(self):

        OPTIONS = ["Adicionar inquilino","Remover inquilino","Modificar imóvel","Adicionar nova tabela","Voltar"]
        function = choose_options(OPTIONS)

        if function == 0:
            print("Adicionar inquilino")

            database = Excel()
            sheets_options = database.sheets

            sheet = choose_options(sheets_options)
            rows = database.read_sheet(sheet)
            property_options = list()
            print("LISTA DE IMÓVEIS:")
            for index, row in enumerate(rows):
                print(f"{index+1}- {row[0]}")
                property_options.append(row[0])
            print("Escolha o imóvel a ser modificado (digite a opção conforme aparece):")
                
            while True:
                property_choice = input().upper()
                if property_choice in property_options:
                    print("Escolha válida")
                    break
                print("Escolha inválida, tente novamente")

            tenent = input("Insira o nome do inquilinho: ")
            start_contract = input("Insira a data de início do contrato (dd/mm/aa): ")
            end_contract = input("Insira a data de fim do contrato (dd/mm/aa): ") #TODO: Insert validation            
            value = input("Insira o valor do aluguel:") #TODO: Insert validation
            #TODO: Continue
            

        if function == 1:
            print("Remover inquilino")

        if function == 2:
            print("Modificar imóvel")

        if function == 3:
            print("Adicionar tabela")

        if function == len(OPTIONS)-1:
            return

    def __str__(self) -> str:
        return f"{self.APP_NAME} | Version: {self.VERSION} | Running"