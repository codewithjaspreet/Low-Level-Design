from abc import ABC, abstractmethod

class PaymentProcessor(ABC) :

    @abstractmethod
    def pay(self, amount: float):
        print(f'paying {amount} successfully')


