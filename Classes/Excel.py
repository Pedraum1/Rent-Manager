import pandas as pd
import os

from Functions.Tables import row_not_null, replace_nan_with_empty, convert_datetime_to_str, sheet_name
from Classes.Models.Apartment import Apartment, ApartmentConfig
from Classes.Models.House import House, HouseConfig
from Classes.Models.Property import Property, Contract
from Classes.Models.Tenant import Tenant

class Excel:
    
    def __init__(self, table_file_name = "Table.xlsx"):
        current_directory = os.path.dirname(os.path.abspath(__file__))

        self.file_path = os.path.join(current_directory, "..", "Tables", table_file_name)
        self.sheets = pd.ExcelFile(self.file_path, engine="openpyxl").sheet_names
    
    def show_data(self):
        for sheet in self.sheets:
            for row in self.read_sheet(sheet):
                print(f'{row[0]:<15}{row[1]:^15}{row[2]:^15}{row[3]:^10}{row[4]:^10}{row[5]:>20}')

    def get_overdue_rents(self,date:str) -> list:
        #returns a list of all rental instances to be charged in the provided date
        rents = self.get_all_rents()
        overdue_rents = list()

        for rent in rents:
            if rent.payday == '':
                continue
            if rent.payday == date:
                overdue_rents.append(rent)

        return overdue_rents

    def get_all_rents(self) -> list:
        rents = list()
        for sheet in self.sheets:
            for row in self.read_sheet(sheet):
                tenant = Tenant(row[5])
                contract = Contract(row[4], row[3], row[1], row[2], tenant)
                apartment_configs = ApartmentConfig(sheet[4:],row[0][-3:])

                apartment = Apartment(apartment_configs, contract)

                rents.append(apartment)
        return rents

    def read_sheet(self, sheet_name:str) -> list:
        sheet_data = list()

        for index, row in self.get_sheet(sheet_name).iterrows():
            linha = row
            linha = linha.to_list()
            if(row_not_null(linha)):
                linha = convert_datetime_to_str(replace_nan_with_empty(linha))
                sheet_data.append(replace_nan_with_empty(linha))

        return sheet_data

    def get_sheet(self, sheet_name:str):
        return pd.read_excel(self.file_path, sheet_name=sheet_name, index_col=None, engine="openpyxl")

    def sheet_len(self, sheet_name:str) -> int:
        return pd.read_excel(self.file_path, sheet_name=sheet_name, engine="openpyxl").shape[0]

    
