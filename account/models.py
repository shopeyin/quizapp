from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager , GroupManager,PermissionManager
from django.contrib.auth.models import Group
from django.utils.text import slugify
from .utils import unique_slug_generator
from django.urls import reverse
from django.db.models.signals import post_delete,pre_save
from django.dispatch import receiver
from django.conf import settings
from django.db import transaction
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





   
class Teacher(models.Model):
    user                 =   models.OneToOneField(MyUser,on_delete=models.CASCADE,primary_key=True) 

    def __str__(self):
        return self.user.username



class Subject(models.Model): 
    name                = models.CharField(max_length=30,unique=True)
    teacher             = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    slug 				= models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.name 

    def get_absolute_url(self):
       return reverse('teacher:view_quiz', args=[str(self.slug)])


def pre_save_subject_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name,instance.slug)
pre_save.connect(pre_save_subject_receiver, sender=Subject)




class Student(models.Model):
    user                 =   models.OneToOneField(MyUser,on_delete=models.CASCADE,primary_key=True) 
    subject             =    models.ManyToManyField(Subject)

    def __str__(self):
        return self.user.username




class Quiz(models.Model):
    question            = models.CharField(max_length=100,unique=True)
    answer              = models.CharField(max_length=100,unique=False)
    subject             = models.ForeignKey(Subject, on_delete=models.CASCADE)
    slug 				= models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.question


  

def pre_save_quiz_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.subject,instance.slug)
pre_save.connect(pre_save_quiz_receiver, sender=Quiz)






