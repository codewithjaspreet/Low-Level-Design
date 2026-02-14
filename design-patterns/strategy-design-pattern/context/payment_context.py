from strategy.payment_strategy import PaymentStrategy
class PaymentContext:

    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy


    def pay(self, amount) :
        self._strategy.pay(amount)


