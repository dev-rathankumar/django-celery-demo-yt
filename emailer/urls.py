from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send-bulk-emails/', views.send_bulk_emails, name='send_bulk_emails'),
]