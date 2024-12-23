from django.db import models
from django.contrib.postgres.fields import ArrayField

'''
All tables and data models used in the app 
'''

# Data of the user's profile
# Primary Key: username
class ProfileData(models.Model):
    username = models.CharField(max_length=100, unique=True)
    profilePicture = models.ImageField(upload_to='profile_pics/')
    friendList = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    winRate = models.FloatField(default=0.0)
    
    def __str__(self): 
        return self.username

# used to temporarily store verification code sent trough smtp.
# Primary Key: username
class VerificationCode(models.Model):
    username = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.username