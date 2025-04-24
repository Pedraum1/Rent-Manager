from os import system
from time import sleep
from abc import ABC, abstractmethod

class Menu(ABC):

    def __init__(self, message:str):
        self.message = message
        self.delay = 1

    @abstractmethod
    def run(self):
        pass

    def clear_terminal(self):
        system('cls')

    def wait(self):
        sleep(self.delay)
