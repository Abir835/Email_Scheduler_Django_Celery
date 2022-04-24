from django.urls import path
from emailsender import views

urlpatterns = [
    path('', views.email_body, name='email-body'),
    path('email-list', views.email_list, name='email-list'),
    path('delete_email/<int:pk>', views.delete_email, name='delete_email')
]