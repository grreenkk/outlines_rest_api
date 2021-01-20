from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings #This is used used to retrieve settings from our settings.py file in settings of our django project


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email) #This ensures the second part of an email is in lowercase"""
        user = self.model(email=email, name=name)
        user.set_password(password) #This ensures that the password in the database is a hash, incase of a hack the password will be seen as a hash(*)"""
        user.save(using=self._db) #This is used to save the created user model in the database"""

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True) #This crates an email
    #feild in our database, while the unique means that all emails must be same"""
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)#This is a feild used to know
    #if a user is activated or not, it being true means at default all of them will be actiavted.
    #But this can also be used to deactivate users"""
    is_staff = models.BooleanField(default=False)#This determines if a user is a staff user and
    #determine if they should have access to the django admin, so setting it to false means they are not staff therefore
    #they shouldnt have access"""

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    #below are function that will help django interact with our customised models"""
    def get_full_name(self):#Because we we are defining a function in a class we have to use self as an attribute"""
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text










# Create your models here.
