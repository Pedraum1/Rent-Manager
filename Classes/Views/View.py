import customtkinter as ctk
from abc import ABC, abstractmethod

class View(ctk.CTk, ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x600")
        self._set_appearance_mode("system")
        self.configure_ui()

    @abstractmethod
    def configure_ui(self):
        pass
    