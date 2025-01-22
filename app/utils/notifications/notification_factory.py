from app.utils.notifications.email_notification_service import EmailNotificationService
# from utils.sms_notification_service import SMSNotificationService (Future implementation)

def get_notification_service(service_type: str):
    """
    Factory method to get the appropriate notification service.

    Args:
        service_type (str): The type of notification service (e.g., 'email', 'sms').

    Returns:
        NotificationService: An instance of the requested notification service.
    """
    if service_type == "email":
        return EmailNotificationService()
    # elif service_type == "sms":
    #     return SMSNotificationService()
    else:
        raise ValueError(f"Unsupported notification service: {service_type}")
