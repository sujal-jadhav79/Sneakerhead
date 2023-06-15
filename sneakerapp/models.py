from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CAT=((1,'Nike'),(2,'Adidas Originals'),(3,"Converse"),(4,'Puma'),(5,'Fila'),(6,"Vans"),(7,'Asics'),(8,'New Balance'))
    name=models.CharField(max_length=50,verbose_name="Product Name")
    cat=models.IntegerField(verbose_name="Brand",choices=CAT)
    price=models.FloatField(verbose_name="Product Price")
    status=models.BooleanField(default=True)
    pimage=models.ImageField(upload_to='image')

   #  def __str__(self):
   #   return self.name
    
class Cart(models.Model):
   uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
   pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='pid')
   qty=models.IntegerField(default=1)

class Order(models.Model):
   order_id=models.IntegerField()
   pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='pid')
   uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
   qty=models.IntegerField()

