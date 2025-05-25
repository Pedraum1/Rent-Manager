if __name__ == "__main__":
    from src.Core.Classes.DataMenu import DataMenu
else:
    from ...Core.Classes.DataMenu import DataMenu

class SettingsView(DataMenu):
    def __init__(self):
        message = "Configurações"
        data = [
            'Nome: J&S Administração de Imóveis - Rent Manager',
            'Versão: 0.0.2',
            'Desenvolvido por: Pedro Paulo',
            'Ano de lançamento: 2025'
        ]
        super().__init__(message, data)