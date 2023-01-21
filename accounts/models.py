from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from django.core.mail import send_mail
import uuid



class User(AbstractUser):
    username = None
    email = models.EmailField( unique=True)
    phone = models.CharField(max_length=12)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True,null=True)
    email_verification_token = models.CharField(max_length=200, null=True, blank=True)
    forget_password_token = models.CharField(max_length=200, null=True,blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def name(self):
        return self.first_name + ' ' + self.last_name


@receiver(post_save, sender=User)
def send_email_token(sender,instance,created, **kwargs):
    if created:
        try:
            subject = "Your email need to verify"
            message = f"Hi, click on the link to verify email http://127.0.0.1:9000/{uuid.uuid4()}"
            email_from = "irfan@gmail.com"
            resipt_list = [instance.email]
            send_mail(subject,message,email_from,resipt_list)
        except Exception as e:
            print(e)