from abc import abstractmethod
import openpyxl as op

class DeleteSheet():

    @abstractmethod
    def handle(repository, sheet_name: str) -> bool:
        try:
            database = op.load_workbook(repository.file_path)

            if not repository._verify_sheet_exists(sheet_name):
                print(f"Error: sheet '{sheet_name}' doesn't exist")
                return False
            
            database.remove(database[sheet_name])
            database.save(repository.file_path)

            return True
            
        except Exception as e:
            print(f"Error: {e}")
            return False