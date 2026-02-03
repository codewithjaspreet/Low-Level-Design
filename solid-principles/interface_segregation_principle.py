# I - Interface Segregation Principle

# The Interface Segregation Principle (ISP) suggests that a class should not be forced to implement methods it doesn’t need


from abc import abstractmethod,ABC


class CreditCardPayment(ABC):
    @abstractmethod
    def process_credit_card_payment(self):
        pass

class PayPalPayment(ABC):
    @abstractmethod
    def process_pay_pal_payment(self):
        pass

class CreditCardProcessor(CreditCardPayment):

    def process_credit_card_payment(self):
        print(f'Processing credit card payment')


class PayPalProcessor(PayPalPayment):

    def process_pay_pal_payment(self):
        print(f'Processing paypal payment')

