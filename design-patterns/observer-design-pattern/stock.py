from observable import Observable
from observer import Observer
from stock_user import EmailAlert, SMSAlert


class Stock(Observable):

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self.price)

    def set_price(self, price: float):
        self.price = price
        self.notify() 


if __name__ == "__main__":
    stock = Stock("AAPL", 90)

    email_alert = EmailAlert()
    sms_alert = SMSAlert()

    stock.attach(email_alert)
    stock.attach(sms_alert)

    stock.set_price(100)
    stock.set_price(120)
