from django.db import models

# Create your models here.
# this is model for Voter 
class Voter(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(default="ps.jpg",upload_to="pics")
    aadhar=models.BigIntegerField(max_length=12)
    address=models.TextField()
    contact=models.BigIntegerField(max_length=10)
    dob=models.DateField()
    
    def __str__(self):
        return self.name