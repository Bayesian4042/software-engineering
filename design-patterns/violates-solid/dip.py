class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")

class SmsService:
    def send_sms(self, message):
        print(f"Sending SMS: {message}")


class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SmsService()

    def send_notification(self, message):
        self.email_service.send_email(message)
        self.sms_service.send_sms(message)