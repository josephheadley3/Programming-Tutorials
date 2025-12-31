from django.db import models


# Create your models here.
class PasswordEntry(models.Model):
    CATEGORY_CHOICES = [
        ('Email', 'Email'),
        ('Work', 'Work'),
        ('Jobs', 'Jobs'),
        ('Coding', 'Coding'),
        ('Health', 'Health'),
        ('Finance', 'Finance'),
        ('Bills', 'Bills'),
        ('Education', 'Education'),
        ('Travel', 'Travel'),
        ('Social Media', 'Social Media'),
        ('Shopping', 'Shopping'),
        ('Entertainment', 'Entertainment'),
        ('Gaming', 'Gaming'),
        ('Other', 'Other'),
    ]

    id = models.AutoField(primary_key=True)
    organization = models.CharField(max_length=254)
    website = models.CharField(max_length=254)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

