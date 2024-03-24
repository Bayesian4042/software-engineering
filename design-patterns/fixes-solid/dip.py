from abc import ABC, abstractmethod

class IMessageService(ABC):
    @abstractmethod
    def send(self, message: str, receiver: str):
        pass

class EmailService(IMessageService):
    def send(self, message: str, receiver: str):
        print(f"Sending email: {message} to {receiver}")

class SmsService(IMessageService):
    def send(self, message: str, receiver: str):
        print(f"Sending SMS: {message} to {receiver}")


class NotificationService:
    def __init__(self, message_service: IMessageService):
        self.message_service = message_service

    def send_notification(self, message: str, receiver: str):
        self.message_service.send(message, receiver)