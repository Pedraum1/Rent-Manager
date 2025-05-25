if __name__ == "__main__":
    from Core.Classes.OptionMenu import OptionMenu
    from src.Views.Rents.RentView import RentView
    from src.Views.CRUD.CrudView import CrudView
    from src.Views.Settings.SettingsView import SettingsView
else:
    from ..Core.Classes.OptionMenu import OptionMenu
    from .Rents.RentView import RentView
    from .CRUD.CrudView import CrudView
    from .Settings.SettingsView import SettingsView

class MenuView(OptionMenu):

    def __init__(self):
        options = ["Verificar alugueis", "Alterar base de dados", "Configurações"]
        super().__init__("Menu", options)

    def execute_function(self, option_index:int):
        match option_index:
            case 0:
                #Rent management
                rent_view = RentView()
                rent_view.run()

            case 1:
                #Database operations (CRUD)
                crud_view = CrudView()
                crud_view.run()

            case 2:
                #Settings
                settings_view = SettingsView()
                settings_view.run()

            case _:
                print("ERRO: Função não reconhecida")

if __name__ == "__main__":
    menu = MenuView()
    menu.run()
            