
from time import sleep
from django.core.mail import send_mail
from celery import shared_task

@shared_task()
def send_feedback_email_task():
    """Sends an email when the feedback form has been submitted."""
    print("hello --------------------")
    print("hello --------------------")
    print("hello --------------------")
    print("hello --------------------")
    print("--------------------")