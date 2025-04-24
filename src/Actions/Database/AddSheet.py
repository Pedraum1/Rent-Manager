from abc import abstractmethod
import pandas as pd

class AddSheet():

    @abstractmethod
    def handle(repository, sheet_name: str, type:str) -> bool:
        header = ['id', 'inicio do contrato', 'final do contrato', 'vencimentos', 'valor do aluguel', 'nome do inquilino']
        
        if not type in repository._property_types:
            print("Error: property type not valid")
            return False

        sheet_name = sheet_name.upper()
        match type:
            case 'APTO':
                sheet_name = 'APTO '+sheet_name
            case 'CASA':
                sheet_name = 'CASA '+sheet_name
            case 'PTCM':
                sheet_name = 'PTCM '+sheet_name
        try:
            new_sheet = pd.DataFrame([header])
            with pd.ExcelWriter(repository.file_path, engine='openpyxl', mode='a', if_sheet_exists='error') as writer:
                new_sheet.to_excel(writer, sheet_name=sheet_name, index=False, header=False)

            return True
        
        except Exception as e:
            print(f"Error: {e}")
            return False