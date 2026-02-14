# main.py

# Factory pattern centralizes object creation logic and removes tight coupling between client and concrete classes.
from factory.notification_factory import NotificationFactory

notification = NotificationFactory.create_notification("email")
notification.send("Hello User")
