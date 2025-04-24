from Classes.Models.Property import Property, Contract

class Store(Property):

    def __init__(self, name:str,  contract:Contract):
        super().__init__(contract)

        self.store_name = name
