import email
from email.message import EmailMessage
from django.db import models 
from django.core.mail import send_mail

# Create your models here.
class Mails(models.Model):
    to = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField()

    def __str__(self):
        return self.to