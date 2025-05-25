from .Menu import Menu
from abc import ABC

class DataMenu(Menu):

    def __init__(self, message:str, data:list):
        super().__init__(message)
        self.data = data
    
    def run(self):
        self.clear_terminal()
        self.wait()
        
        #Display data
        print(self.message)
        for index, info in enumerate(self.data):
            print(f"{index}. {info}")

        #Condition to end function
        input("Pressione Enter para prosseguir")