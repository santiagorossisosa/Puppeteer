from app.utils.notifications.notification_service import NotificationService
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

class SMSNotificationService(NotificationService):
    #TO DO