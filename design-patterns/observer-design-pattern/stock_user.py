from observer import Observer

class EmailAlert(Observer):
    def update(self, price:str):
        print(f"Email Alert: Stock price updated to {price}")


class SMSAlert(Observer):
    def update(self, price):
        print(f"SMS Alert: Stock price updated to {price}")
