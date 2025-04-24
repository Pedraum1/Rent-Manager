from Classes.Models.Property import Property, Contract

class House(Property):

    def __init__(self, street:str, number:str, contract:Contract):
        super().__init__(contract)

        self.street = street
        self.number = number