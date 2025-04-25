from src.Core.Classes.Date import Date
from abc import ABC
from dataclasses import dataclass

@dataclass
class PropertyDTO:
    rent: int
    payday: Date
    contract_start: Date
    contract_end: Date
    tenant: str
    property_type: str
    rented: bool = True

class Property(ABC):

    def __init__(self, configs: PropertyDTO):
        self.rent = configs.rent
        self.payday = configs.payday
        self.contract_start = configs.contract_start
        self.contract_end = configs.contract_end
        self.tenant = configs.tenant
        self.rented = configs.rented