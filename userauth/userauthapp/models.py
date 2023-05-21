from django.db import models

# Create your models here.

class user(models.Model):
    cust_id:models.IntegerField
    cust_name:models.CharField
    cust_add:models.CharField
    cust_phn:models.IntegerField
    cust_username:models.CharField
    cust_password:models.CharField