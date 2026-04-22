from abc import abstractmethod, ABC

class LegacyPay(ABC):

    def make_payment(self , value:float):
        print(f"Paid {value} using LegacyPay system")
