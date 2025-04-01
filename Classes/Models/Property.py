from Classes.Date import Date
from Tenant import Tenant
from abc import ABC
from dataclasses import dataclass

@dataclass
class Contract:
    rent: int
    payday: Date
    contract_start: Date
    contract_end: Date
    tenant: Tenant
    rented: bool

class Property(ABC):

    def __init__(self, configs: Contract):
        self.rent = configs.rent
        self.payday = configs.payday
        self.contract_start = configs.contract_start
        self.contract_end = configs.contract_end
        self.tenant = configs.tenant
        self.rented = configs.rented