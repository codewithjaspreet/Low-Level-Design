from notificaiton.notification import Notification

class EmailNotification(Notification):

    def send(self, message: str):
        print(f"Sending Email: {message}")
