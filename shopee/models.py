from django.db import models

# Create your models here.
class Product(models.Model):
    p_title = models.CharField(max_length=100)
    p_description = models.CharField(max_length=100)
    p_prize = models.IntegerField()
    p_image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.p_title


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

  

    @property
    def totalprice(self):
        return self.product.p_prize * self.quantity



    def __str__(self):
        return self.product.p_title




class Order(models.Model):
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=100)

    @property
    def total(self):
        return self.subtotal + self.shipping


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)



# class User(models.Model):
    
