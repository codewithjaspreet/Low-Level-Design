# # Strategy Pattern - allows you to define a family of algorithms, encapsulate each one, and make them interchangeable.

# Use Strategy when:
# You have multiple ways to perform the same task
# You see too many if-else or switch statements
# You want to follow Open/Closed Principle
# Behavior must change at runtime

from strategy.credit_card import CreditCardPayment
from strategy.paypal import PayPalPayment
from strategy.upi import UPIPayment
from context.payment_context import PaymentContext

context = PaymentContext(CreditCardPayment())
context.pay(100)

context.set_strategy(PayPalPayment())
context.pay(200)

context.set_strategy(UPIPayment())
context.pay(300)

