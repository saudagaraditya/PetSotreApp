from django.db import models
from petsapp.models import pets
from django.contrib.auth.models import User

# Create your models here.

class Payment(models.Model):
    payment_id = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount_paid = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id
    
class Orders(models.Model):
    status = (
        ('new','new'),
        ('pending','Pending'),
        ('delivery','delivery'),
        ('cancelled','cancelled'),
    )

    states = (
        ('AP','Andhra Pradesh'),
        ('AR','Arunachal Pradesh'),
        ('AS','ASSAM'),
        ('BR','Bihar'),
        ('Goa','Goa'),
        ('GJ','Gujrat'),
        ('RJ','Rajastan'),
        ('UP','Uttar Pradeh'),
        ('MH','Maharahtra'),
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    order_number = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100,choices=states)
    country = models.CharField(max_length=100)
    total = models.FloatField
    status = models.CharField(max_length=100,choices=status)
    ip = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name
    

class OrderPet(models.Model):
    order_id = models.ForeignKey(Orders,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    pet_name = models.ForeignKey(pets,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    pet_price = models.FloatField()
    is_ordered =models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.pet.pet_name