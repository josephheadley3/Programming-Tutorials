from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('create_password_entry/', views.create_password_entry, name='create_password_entry'),
    path('show_password_entries/', views.show_password_entries, name='show_password_entries'),
    path('review_password_entry/', views.preview_password_entry, name='review_password_entry'),
    path('confirm_password_entry/', views.confirm_password_entry, name='confirm_password_entry'),
]