from abc import ABC, abstractmethod

class Dicount(ABC):
    @abstractmethod
    def calculate(self, amount):
        pass


class NoDiscount(Discount):
    def calculate(self, amount):
        return amount
    

class PercentageDiscount(Discount):
    def __init__(Self, percentage):
        self.percentage = percentage

    def calculate(self, amount):
        return amount - (amount * self.percentage / 100)
    
