from Functions.Inputs import *


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
            if function == 0 :
                print("Encontrando imóveis vencidos")
            if function == 1 :
                print("Registros")
            if function == 2 :
                print(self)
            if function == len(self.OPTIONS)-1:
                return

            input("Pressione qualquer tecla para prosseguir")
            clear()

    def __str__(self) -> str:
        return f"{self.APP_NAME} | Version: {self.VERSION} | Running"