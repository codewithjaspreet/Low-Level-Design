from strategy.payment_strategy import PaymentStrategy

class UPIPayment(PaymentStrategy):

    def pay(self,amount):
        print(f"Paid {amount} using UPI")
