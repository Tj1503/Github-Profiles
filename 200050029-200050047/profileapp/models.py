from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers=models.IntegerField(default=0)
    timeoflastupdate=models.DateTimeField(auto_now=True)

class Repository(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    reponame=models.CharField(max_length=100,default='')
    stars=models.IntegerField(default=0)

    class Meta:
        ordering=['stars']

def create_profilepage(sender, **kwargs):
    if kwargs['created']:
        user_profile=Profile.objects.create(user=kwargs['instance'])
        user_profile.save()
        profile=Profile.objects.get(user=kwargs['instance'])
        repos=Repository.objects.create(profile=profile)
        repos.save()


    

post_save.connect(create_profilepage,sender=User)
