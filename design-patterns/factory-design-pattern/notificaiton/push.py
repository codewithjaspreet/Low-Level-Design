from notificaiton.notification import Notification

class PushNotification(Notification):

    def send(self, message: str):
        print(f"Sending Push Notification: {message}")
