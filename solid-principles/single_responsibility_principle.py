
# S - Single Responsibility Principle
# A class should have only one reason to change , one class = one job

class NotificationService:
    def __init__(self,sender) -> None:
        self.sender = sender

    def notify_user(self,message):
        self.sender.send(message)


    class EmailSender:

        def send(self, message):
            print(f'Sending email with a message , {message}')

    class SmsSender:

        def send(self, message):
            print(f'Sending sms - {message}')
