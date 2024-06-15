from django.conf import settings
from django.core.mail import send_mail


def send_activation_email(email, email_token):
    subject = 'Your account needs to be activated'
    email_from = settings.EMAIL_HOST_USER
    message = f'Hi! Click on the link to activate your account http://127.0.0.1:8000/accounts/activate_account/{email_token}'

    try:
        send_mail(subject, message, email_from, [email])
        print(f"email sent to {email}")
    except Exception as e:
        print(e)
