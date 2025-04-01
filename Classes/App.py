from Functions.Inputs import *
from Functions.Tables import today
from Functions.Prints import *
from Classes.Excel import Excel
class App:
    def __init__(self):
        self.APP_NAME = "Rent Manager | J&S - Administração de Imóveis"
        self.VERSION = "0.0.1"
        self.OPTIONS = ["Encontrar alugueis vencidos", "Registros", "Informações", "Sair do Aplicativo"]

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
                
            if function == 1 :
                excel = Excel()
                excel.show_data()

            if function == 2 :
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
            print_apartments(excel.get_overdue_rents(today()))
            
        if function == 1:
            excel = Excel()
            date = input_date("Digite a data a qual deseja pesquisar no formato dd/mm/yyyy:")
            print_apartments(excel.get_overdue_rents(date))

        if function == len(OPTIONS)-1:
            return

    def __str__(self) -> str:
        return f"{self.APP_NAME} | Version: {self.VERSION} | Running"