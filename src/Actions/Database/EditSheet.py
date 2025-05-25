import openpyxl as op

class EditSheet():

    @staticmethod
    def handle(repository, sheet_name: str, new_name: str, type:str) -> bool:
        try:
            database = op.load_workbook(repository.file_path)

            if type == None:
                type = sheet_name[:4]

            #Error handling

            #does some sheet already have the new name?
            if repository._verify_sheet_exists(new_name):
                print(f"Error: The database already have a sheet named '{sheet_name}'")
                return False

            #the new name is equals to previous one?
            if sheet_name == new_name:
                print(f"Error: the new name is the same as the old one")
                return False     

            #the property type is valid?
            if not repository._verify_property_type(type):
                print(f"Error: the type '{type}' is not valid")
                return False
            
            if new_name == None:
                new_name = sheet_name[5:]
            
            sheet = database[sheet_name]
            sheet.title = f'{type} {new_name}'
            database.save(repository.file_path)

            return True
            
        except Exception as e:
            print(f"Error: {e}")
            return False