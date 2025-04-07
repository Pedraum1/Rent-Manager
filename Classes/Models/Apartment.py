from Classes.Models.Property import Property, Contract

class Apartment(Property):

    def __init__(self, condominium:str, number:str, contract:Contract):
        super().__init__(contract)

        self.condominium = condominium
        self.number = number