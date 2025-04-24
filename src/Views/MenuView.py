from Core.Classes.OptionMenu import OptionMenu

class MenuView(OptionMenu):

    def __init__(self):
        options = ["Verificar alugueis", "Alterar base de dados", "Configurações"]
        super().__init__("Menu", options)

    def execute_function(self, option_index:int):
        match option_index:
            case 0:
                #Rent manage view
                pass

            case 1:
                #Database operations (CRUD)
                pass

            case 2:
                #Settings
                pass

            case _:
                print("ERRO: Função não reconhecida")

if __name__ == "__main__":
    menu = MenuView()
    menu.run()
            