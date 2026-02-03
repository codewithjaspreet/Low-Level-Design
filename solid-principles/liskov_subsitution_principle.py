
# L  - object of a superclass should be able to be replaced with objects of sub class without affecting the correctness of the sub program

from abc import ABC, abstractmethod

class IOColor(ABC):
    @abstractmethod
    def print_color(self, color_name):
        pass


class Green(IOColor):
    def print_color(self, color_name):
        print(f'color is {color_name}')


class Red(IOColor):
    def print_color(self, color_name):
        print(f'color is {color_name}')
