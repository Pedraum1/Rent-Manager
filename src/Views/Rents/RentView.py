if __name__ == "__main__":
    from src.Core.Classes.OptionMenu import OptionMenu
    #from Views.RentDataView import RentDataView
else:
    from ...Core.Classes.OptionMenu import OptionMenu
    #from .RentDataView import RentDataView

class RentView(OptionMenu):
    def __init__(self):
        options = ["Alugueis para cobrar hoje", "Verificar data específica"]
        super().__init__("Menu", options)

    def execute_function(self, option_index:int):
        #rents = RentDataView()
        match option_index: 
            case 0:
                #TODO: Insert get today function
                #rents.run(today())
                print("Alugueis para cobrar hoje")
            case 1:
                #TODO: Insert get date function
                #rents.run(date())
                print("Verificar data específica")

            case _:
                print("ERRO: Função não reconhecida")