from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    photo=models.ImageField(upload_to='pic/')
    bio=models.TextField()
    username=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    last_name=models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    phone_number=models.IntegerField(null=True)
    email=models.EmailField()
    
    
    def save_profile(self):
        self.save()
    def delete_profile(self):
       self.delete()

    def update_bio(self,bio):
         self.bio=bio
         self.save()
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(username=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()
class Neighbourhood(models.Model):
     neighbourh_name=models.CharField(max_length=100)
     neighbourh_location= models.CharField(max_length=200)
     occupants=models.IntegerField(null=True)
     profile=models.ForeignKey(Profile,null=True)
     def __str__(self):
        return self.name
     @classmethod
     def create_neighbourhood(cls,name,loc,occupants):
        neighborhood=Neighborhood(name=name,location=loc,occupants=occupants)
        return neighborhood
     
     @classmethod
     def find_neighbourhood(cls,id):
        neighborhood=cls.objects.get(id=id)
        return neighborhood
     def save_neighbourhod(self):
         self.save()

     def delete_neighbourhood(self):
       self.delete()


    
       