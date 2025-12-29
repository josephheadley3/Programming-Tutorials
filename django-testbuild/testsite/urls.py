from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('create_password_entry/', views.create_password_entry, name='create_password_entry'),
]