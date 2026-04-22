from payment_processor import PaymentProcessor
from legacy_pay import LegacyPay
class PaymentAdapter(PaymentProcessor):

    def __init__(self,  legacy_pay: LegacyPay):
        self._legacy_pay = legacy_pay

    def make_payment(self , amount:float):
        self._legacy_pay.make_payment(amount)


