
# O — Open/Closed Principle (OCP)
# Software entities should be open for extension but closed for modification.

from abc import abstractmethod, ABC

class NotificationService(ABC):
    @abstractmethod
    def send(self,message):
     pass


class EmailSender(NotificationService):

    def __init__(self) -> None:
       super().__init__()

    def send(self,message):
        print(f'sending email with a message - {message} ')


class SMSSender(NotificationService):

    def send(self, message):
        print(f"Sending SMS: {message}")

class PushSender(NotificationService):
    def send(self, message):
        print(f"Sending PUSH: {message}")
