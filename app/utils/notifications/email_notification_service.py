from app.utils.notifications.notification_service import NotificationService
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

class EmailNotificationService(NotificationService):
    def __init__(self):
        self.smtp_server = os.getenv("MAIL_SERVER", "smtp.mailtrap.io")
        self.smtp_port = int(os.getenv("MAIL_PORT", 587))
        self.smtp_username = os.getenv("MAIL_USERNAME", "")
        self.smtp_password = os.getenv("MAIL_PASSWORD", "")
        self.mail_from = os.getenv("MAIL_FROM", "no-reply@example.com")
        self.use_tls = os.getenv("MAIL_USE_TLS", "True") == "True"

    async def send_notification(self, recipient: str, subject: str, body: str):
        """
        Send an email asynchronously.

        Args:
            recipient (str): Recipient email address.
            subject (str): Subject of the email.
            body (str): Body content of the email.

        Returns:
            None
        """
        try:
            # Create email message
            msg = MIMEMultipart()
            msg["From"] = self.mail_from
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.use_tls:
                    server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.sendmail(self.mail_from, recipient, msg.as_string())

        except Exception as e:
            print(f"Failed to send email to {recipient}: {str(e)}")