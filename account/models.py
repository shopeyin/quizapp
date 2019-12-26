from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager , GroupManager,PermissionManager
from django.contrib.auth.models import Group
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        
        user = self.model(
               email = self.normalize_email(email),
               username=username,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, password):
        user = self.create_user(
               email=self.normalize_email(email),
               password=password, 
               username=username,
            )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




class MyUser(AbstractBaseUser,PermissionsMixin):
    email                   = models.EmailField(verbose_name="email", max_length=60,unique=True)  
    username                = models.CharField(max_length=30,unique=True)
    date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_student              = models.BooleanField('student status', default=False)
    is_teacher              = models.BooleanField('teacher status', default=False)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects=MyUserManager()

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.email


class Subject(models.Model):
    subject                = models.CharField(max_length=30)

    def __str__(self):
        return self.subject


class Student(models.Model):
    user                 =   models.OneToOneField(MyUser,on_delete=models.CASCADE,primary_key=True) 
    interests            =   models.ManyToManyField(Subject, related_name='interested_students')      

    def __str__(self):
        return self.user 





