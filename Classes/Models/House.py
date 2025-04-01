from .Property import Property, Contract
from ..Date import Date

from dataclasses import dataclass

@dataclass
class HouseConfig:
    street: str
    street_number: int

class House(Property):

    def __init__(self, configs:HouseConfig, contract:Contract):
        super().__init__(contract);

        self.street = configs.street
        self.street_number = configs.street_number