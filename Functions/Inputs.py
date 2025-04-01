from .Commands import *
from Classes.Date import Date

def choose_options(options:list, message:str = "Escolha dentre as opções:", return_type:str = "int"):
    option = False
    while not option:
        clear()

        for index, option in enumerate(options):
            print(f"{index} - {option}")
        print(message)
        option = input().lower()

        if hasOption(option):
            match return_type:
                case "string":
                    return option
                case "int":
                    return int(option)
                case "bool":
                    return bool(int(option))
                case _:
                    return int(option)

        print("ERRO: Opção escolhida é inválida")
        option = False
        wait(2)

def hasOption(choice:str)->bool:
    try:
        int(choice)
        return True
    except ValueError:
        return False
    
def input_date(message:str = "Insira a data")->str:
    inputed_date = input(message)
    try:
        inputed_date = Date(inputed_date)
        return str(inputed_date)
    except:
        return input_date(message)