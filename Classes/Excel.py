import pandas as pd
from Functions.Tables import row_not_null, replace_nan_with_empty, convert_datetime_to_str
import os

class Excel:
    def __init__(self, table_file_name = "Table.xlsx"):
        current_directory = os.path.dirname(os.path.abspath(__file__))

        self.file_path = os.path.join(current_directory, "..", "Tables", "Table.xlsx")
        self.sheets = pd.ExcelFile(self.file_path, engine="openpyxl").sheet_names

    def print_sheet(self, sheet_name:str):
        print(pd.read_excel(self.file_path, sheet_name=sheet_name, engine="openpyxl"))

    def get_sheet(self, sheet_name:str):
        return pd.read_excel(self.file_path, sheet_name=sheet_name, index_col=None, engine="openpyxl")

    def sheet_len(self, sheet_name:str) -> int:
        return pd.read_excel(self.file_path, sheet_name=sheet_name, engine="openpyxl").shape[0]

    def read_sheet(self, sheet_name:str) -> list:
        sheet_data = list()

        for index, row in self.get_sheet(sheet_name).iterrows():
            linha = row
            linha = linha.to_list()
            if(row_not_null(linha)):
                linha = convert_datetime_to_str(replace_nan_with_empty(linha))
                sheet_data.append(replace_nan_with_empty(linha))

        return sheet_data

    def read_row(self, sheet:str, index:int):
        if(index < 0):
            raise ValueError("Value must be greater or equals to 0")
        return self.read_sheet(sheet)[index]

if __name__ == "__main__":
    tabela = Excel()
    folha = tabela.sheets[0]
    sheet = tabela.read_sheet(folha)
    for row in range(0,tabela.sheet_len(folha)):
        print(tabela.read_row(folha, row))