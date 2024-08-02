from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

# Customer Model
class Customer(AbstractUser):
    username = None 
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255)
    country = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name


# Navbar
class Navbar(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    target = models.CharField(max_length=150, null=False, blank=False)
    offset = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

# Slider
class HeroSlider(models.Model):
    heading = models.CharField(max_length=150, null=False, blank=False)
    paragraph = models.TextField(null=True)

    def __str__(self):
        return self.heading


# About
class About(models.Model):
    icon = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=150, null=False, blank=False)
    subtitle = models.TextField(null=True)

    def __str__(self):
        return self.title


# About
class Achievement(models.Model):
    icon = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=150, null=False, blank=False)
    award = models.IntegerField(default=0)

    def __str__(self):
        return self.title


# Class
class Class(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='classes/',max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


# Trainers
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='trainers/')
    social_links = models.JSONField()

    def __str__(self):
        return self.name


# Membership
class Membership(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    benefits = models.JSONField()

    def __str__(self):
        return self.title


# Testimonial
class Testimonial(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    message = models.TextField(null=True)
    image = models.ImageField(upload_to='testimonial/',max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


# Blogs
class Blog(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    link = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='blog/',max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def formatted_date(self):
        return self.date.strftime('%B %d, %Y') if self.date else ''


# Brands
class Brand(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    link = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='brand/',max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


# Footer Galler Image
class FooterGallery(models.Model):
    image = models.ImageField(upload_to='footer/gallery/', max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Image {self.id}"


# Footer
class Footer(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    logo = models.ImageField(upload_to='footer/logo/',max_length=255, null=True, blank=True)
    location = models.CharField(max_length=100, null=False, blank=False)
    contact = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True)
    benefits = models.JSONField()
    gallery = models.ManyToManyField(FooterGallery, related_name='footers', blank=True)
    newsletter = models.CharField(max_length=100, null=True, blank=True)
    social_links = models.JSONField(null=True, blank=True)
    copyright = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title