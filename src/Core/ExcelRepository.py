import os
import pandas as pd

if __name__ == "__main__":
    #Database Classes
    from DatabaseRepository import DatabaseRepository
    from src.Models.Property import Property, PropertyDTO

    #Actions
    from src.Actions.Database.AddSheet import AddSheet
    from src.Actions.Database.DeleteSheet import DeleteSheet
    from src.Actions.Database.EditSheet import EditSheet
else:
    #Database Classes
    from .DatabaseRepository import DatabaseRepository
    from src.Models.Property import Property, PropertyDTO

    #Actions
    from ..Actions.Database.AddSheet import AddSheet
    from ..Actions.Database.DeleteSheet import DeleteSheet
    from ..Actions.Database.EditSheet import EditSheet

class ExcelRepository(DatabaseRepository):
    def __init__(self, table_file_name:str = "Table.xlsx"):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(current_directory, "..", "Tables", table_file_name)
        self.connect_with_database()
        self._property_types = ['APTO', 'CASA', 'PTCM']

    #public methods
    def connect_with_database(self):
        sheets = dict()
        sheets_names = pd.ExcelFile(self.file_path, engine="openpyxl").sheet_names

        for sheet_name in sheets_names:
            pandas_sheet = pd.read_excel(self.file_path, sheet_name)
            sheets[sheet_name] = pandas_sheet
        self.sheets = sheets

    def get_overdue_rents(self, date:str):
        #TODO: Create get_overdue_rents function
        pass

    def get_property_by_id(self):
        #TODO: Create get_property_by_id function
        pass

    def get_all_properties(self) -> list:
        #TODO: Create get_all_properties function
        pass

    def add_tenant(self, property_id, tenant_data) -> bool:
        #TODO: Create add_tenant function
        pass

    def delete_tenant(self, property_id, tenant_data) -> bool:
        #TODO: Create delete_tenant function
        pass

    def update_tenant(self, property_id, tenant_data) -> bool:
        #TODO: Create update_tenant function
        pass

    def add_property(self, property: Property, dto:PropertyDTO):
        #TODO: Create add_property function
        pass

    def update_property(self, sheet_name: str, property_id: str, property_data: dict) -> bool:
        #TODO: Create update_property function
        pass

    def add_sheet(self, sheet_name: str, type:str) -> bool:
        try:
            AddSheet.handle(self, sheet_name, type)
            self.connect_with_database()
            return True
        except Exception:
            return False

    def delete_sheet(self, sheet_name: str)->bool:
        try:
            DeleteSheet.handle(self, sheet_name)
            self.connect_with_database()
            return True
        except Exception:
            return False

    def edit_sheet(self, sheet_name: str, new_name:str = None, type:str = None) -> bool:
        try:
            EditSheet.handle(self, sheet_name, new_name, type)
            self.connect_with_database()
            return True
        except Exception:
            return False


    #private methods

    def _verify_property_type(self, property_type:str) -> bool:
        return property_type in self._property_types
    
    def _verify_sheet_exists(self, sheet_name:str) -> bool:
        return sheet_name in self.sheets

if __name__ == "__main__":
    excel = ExcelRepository()

    add = excel.add_sheet("test 3", "APTO")
    result = excel.edit_sheet("APTO TEST 3", type= "APTO")
    delete = excel.delete_sheet("APTO TEST 3")
    print(f"{add} {result} {delete}")