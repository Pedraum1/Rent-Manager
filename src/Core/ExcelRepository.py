import os
import pandas as pd
import openpyxl as op

if __name__ == "__main__":
    from DatabaseRepository import DatabaseRepository
    from Actions.Database.AddSheet import AddSheet
else:
    from .DatabaseRepository import DatabaseRepository
    from ..Actions.Database.AddSheet import AddSheet

class ExcelRepository(DatabaseRepository):
    
    def __init__(self, table_file_name:str = "Table.xlsx"):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(current_directory, "..", "Tables", table_file_name)
        self.connect_with_database()
        self._property_types = ['APTO', 'CASA', 'PTCM']

    def get_overdue_rents(self, date:str):
        pass
    
    def connect_with_database(self):
        self.sheets = dict()
        sheets_names = pd.ExcelFile(self.file_path, engine="openpyxl").sheet_names

        for sheet_name in sheets_names:
            pandas_sheet = pd.read_excel(self.file_path, sheet_name)
            self.sheets[sheet_name] = pandas_sheet

    def get_property_by_id(self):
        pass

    def get_all_properties(self) -> list:
        pass

    def add_tenant(self, property_id, tenant_data) -> bool:
        pass

    def delete_tenant(self, property_id, tenant_data) -> bool:
        pass

    def update_tenant(self, property_id, tenant_data) -> bool:
        pass

    def update_property(self, sheet_name: str, property_id: str, property_data: dict) -> bool:
        pass

    def add_sheet(self, sheet_name: str, type:str) -> bool:
        return(AddSheet.handle(self, sheet_name, type))
    
    def delete_sheet(self, sheet_name: str)->bool:
        try:
            database = op.load_workbook(self.file_path)

            if not self._verify_sheet_exists(sheet_name):
                print(f"Error: sheet '{sheet_name}' doesn't exist")
                return False
            
            database.remove(database[sheet_name])
            database.save(self.file_path)

            return True
            
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def _verify_property_type(self, property_type:str) -> bool:
        return property_type in self._property_types
    
    def _verify_sheet_exists(self, sheet_name:str) -> bool:
        return sheet_name in self.sheets

if __name__ == "__main__":
    excel = ExcelRepository()

    excel.add_sheet("test", "APTO")
    excel.delete_sheet("APTO TEST")