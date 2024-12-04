
from abc import ABC,abstractmethod


class Editors(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class Vscode(Editors):

    def open(self):
        print("vscode open method")

    def write(self):
        print("vscode write method")

    def debug(self):
        print("vscode debug method")

    def execute(self):
        print("vscode execute method")


Vscode_instance=Vscode()

Vscode_instance.open()
    