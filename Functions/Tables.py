from datetime import datetime
from pandas import Timestamp

def row_not_null(row:list) -> bool:
    counter = 0
    for item in row:
        if is_nan(item):
            counter = counter + 1

    if counter == len(row):
        return False
    return True

def replace_nan_with_empty(row:list) -> list:
    for index, item in enumerate(row):
        if is_nan(item):
            row[index] = ""

    return row

def is_nan(value) -> bool:
    return value != value

def convert_datetime_to_str(row:list) -> list:
    for index, value in enumerate(row):
        if type(value) == datetime or type(value) == Timestamp:
            data = value.strftime('%d/%m/%Y')
            row[index] = data
    return row

def today() -> str:
    data_hoje = datetime.today().date()
    data_hoje = int(data_hoje.strftime('%d'))
    return data_hoje

def sheet_name(sheet:str):
    return sheet[4:]
