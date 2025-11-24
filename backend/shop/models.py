from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    #One-to-One
    #Один пользователь одтн покупатель
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=14)
    adress = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    creat_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOISE = [
        ('Оформлен','Оформлен'),
        ('Собирается','Собирается'),
        ('В пути','В пути'),
        ('Доставлен в пунк выдачи','Доставлен в пункт выдачи'),

    ]        
    

    castomer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    status = models.CharField(max_length=50,choices=STATUS_CHOISE,default='Оформлен')
    creat_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"заказ продан {self.castomer}"