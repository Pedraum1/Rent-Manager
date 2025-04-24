from abc import ABC, abstractmethod

class DatabaseRepository(ABC):

    @abstractmethod
    def connect_with_database(self):
        pass

    @abstractmethod
    def get_property_by_id(self):
        pass

    @abstractmethod
    def get_all_properties(self) -> list:
        pass

    @abstractmethod
    def get_overdue_rents(self, date) -> list:
        pass

    @abstractmethod
    def add_tenant(self, property_id, tenant_data) -> bool:
        pass

    @abstractmethod
    def delete_tenant(self, property_id, tenant_data) -> bool:
        pass

    @abstractmethod
    def update_tenant(self, property_id, tenant_data) -> bool:
        pass

    @abstractmethod
    def update_property(self, sheet_name: str, property_id: str, property_data: dict) -> bool:
        pass

    @abstractmethod
    def add_sheet(self, sheet_name: str, type:str) -> bool:
        pass

    def delete_sheet(self, sheet_name: str)->bool:
        pass