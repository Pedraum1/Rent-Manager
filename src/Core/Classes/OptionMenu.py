if __name__ == "__main__":
    from Menu import Menu
else:
    from .Menu import Menu
from abc import ABC, abstractmethod

class OptionMenu(Menu, ABC):

    def __init__(self, message:str, options:list):
        super().__init__(message)
        self.options = options
        self.options.append('Voltar')
    
    def run(self) -> None:
        while True:
            self.clear_terminal()
            self.wait()

            while True:
                #Display options
                print(f"{self.message}\n")
                for index, info in enumerate(self.options):
                    print(f"{index}. {info}")
                response = input(f"\nEscolha uma ação (0 - {len(self.options)-1})\n")

                #validate input
                if(self.validate_option(response)):
                    break
                print(f'"{response}" não é uma resposta válida, escolha novamente')
                self.wait()
                self.clear_terminal()
            response = int(response)
            #Condition to end function
            if response == len(self.options)-1:
                self.wait()
                self.clear_terminal()
                return
            
            self.execute_function(response)

    def validate_option(self, choice:str):
        try:
            choice_index = int(choice)
            return 0 <= choice_index < len(self.options)
        except ValueError:
            return False
    
    @abstractmethod
    def execute_function(self, option_index:int):
        pass