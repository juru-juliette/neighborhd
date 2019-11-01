from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Profile(models.Model):
    photo=models.ImageField(upload_to='pic/')
    bio=models.TextField()
    username=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    email=models.EmailField()
    def save_profile(self):
        self.save()
    def delete_profile(self):
       self.delete()

    def update_bio(self,bio):
         self.bio=bio
         self.save()
class Neighbourhood(models.Model):
     neighbourh_name=models.CharField(max_length=100)
     neighbourh_location= models.CharField(max_length=200)
     occupants_counts=models.IntegerField(null=True)
     profile=models.ForeignKey(Profile,null=True)
     def save_neighbourhod(self):
         self.save()

     def delete_neighbourhood(self):
       self.delete()


    
       