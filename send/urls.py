from django.urls import path
from . import views

urlpatterns = [
    path('api/mails/', views.MailsList.as_view())
]