from .Property import Property, Contract
from ..Date import Date

from dataclasses import dataclass

@dataclass
class ApartmentConfig:
    condominium: str
    apartment_number: int
    block: str = 'a'

class Apartment(Property):

    def __init__(self, configs:ApartmentConfig, contract:Contract):
        super().__init__(contract);

        self.condominium = configs.condominium
        self.apartment_number = configs.apartment_number