from .Commands import *

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