from notificaiton.notification import Notification
class SMSNotification(Notification):

    def send(self, message: str):
        print(f"Sending SMS: {message}")
