from abc import ABC, abstractmethod

class NotificationService(ABC):
    """
    Abstract base class for notification services.
    Provides a common interface for different notification methods (e.g., Email, SMS).
    """

    @abstractmethod
    async def send_notification(self, recipient: str, subject: str, body: str):
        """
        Abstract method to send a notification.

        Args:
            recipient (str): Recipient of the notification.
            subject (str): Subject of the notification.
            body (str): Body content of the notification.

        Returns:
            None
        """
        pass