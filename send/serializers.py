from dataclasses import field
from rest_framework import serializers
from .models import Mails


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mails
        fields = ('to','subject','message')