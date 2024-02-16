from django.db import models
from django.urls import reverse

# Create your models here.
# from django.contrib.auth.models import User
class About(models.Model):
    facilityName = models.CharField(max_length=100)
    faciltyDesc = models.CharField(max_length=255, blank=True)
    facilitDescExtra = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=100,blank=True)
    phoneNumber = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=254, blank=True)
    website = models.URLField(max_length=200, blank=True)


    class Meta:
        verbose_name = ("About")
        verbose_name_plural = ("Abouts")

    def __str__(self):
        return self.facilityName

    def get_absolute_url(self):
        return reverse("About_detail", kwargs={"pk": self.pk})


class Department(models.Model):
    departmentName = models.CharField(max_length=255, blank=False, null=False)
    departmentDesc = models.CharField(max_length=255, blank=True, null=False)
    realdept = models.BooleanField(blank=True, null=False)
    departmentImg = models.CharField(blank=True, max_length=255)
    
    def __str__(self):
        return self.departmentName + " " 

class Service(models.Model):
    serviceTitle = models.CharField(max_length=50)
    serviceDesc = models.CharField (max_length=255)
    realserv = models.BooleanField(null=False)
    logoimg = models.CharField (blank=True,max_length=255)
    placeholderImg = models.CharField(blank=True, max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")
        ordering = ['-serviceTitle', '-department']

    def __str__(self):
        return self.serviceTitle

    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})

class Appointment(models.Model):
    sirName = models.CharField(blank=True,max_length=255)
    firstName = models.CharField(blank=True,max_length=255)
    telContact = models.CharField(blank=True,max_length=255)
    email = models.CharField(blank=True,max_length=255)
    department = models.CharField(blank=True,max_length=255)
    appointmentDate = models.DateField(blank=True, null=True)
    appointmentTime = models.CharField(blank=True,max_length=255)
    amessage = models.TextField(max_length=255)
    
    class Meta:
        ordering = ['-appointmentDate', '-department']

    
    def __str__(self):
        return self.sirName  

class ContactUs(models.Model):
    names = models.CharField(max_length=255)
    email = models.CharField(blank=True, max_length=255)
    subject = models.CharField(blank=True,max_length=255)
    message = models.TextField(blank=True,max_length=255)
    mailingDate = models.DateField(auto_now_add=True)
    phonecontact = models.CharField(max_length=15)

class SubscribeMail(models.Model):
    email = models.CharField(blank=True, max_length=255, unique=True)

    class Meta:
        verbose_name = ("SubscribeMail")
        verbose_name_plural = ("SubscribeMails")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("SubscribeMails_detail", kwargs={"pk": self.pk})


class Carousel(models.Model):
    carouselTitle = models.CharField(max_length=255, blank=True)
    carouselsubTitle = models.CharField(max_length=255, blank=True)
    carouselImg = models.CharField(max_length=255, blank=True)
    placeholderurl = models.URLField(max_length=200, blank=True)

    class Meta:
        verbose_name = ("Carousel")
        verbose_name_plural = ("Carousels")

    def __str__(self):
        return self.carouselTitle

    def get_absolute_url(self):
        return reverse("Carousel_detail", kwargs={"pk": self.pk})
    
class Doctor(models.Model):
    drname = models.CharField(max_length=55, blank=True)
    drspecialty = models.CharField(max_length=55, blank=True)
    drbio = models.CharField(max_length=255, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    drimage = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = ("Doctor")
        verbose_name_plural = ("Doctors")

    def __str__(self):
        return self.drname

    def get_absolute_url(self):
        return reverse("Doctor_detail", kwargs={"pk": self.pk})

class Testimony(models.Model):
    author = models.CharField(blank=True, max_length=50)
    occupation = models.CharField(blank=True, max_length=50)
    testimony = models.TextField(blank=True)
    authorimg = models.CharField(blank=True, max_length=50)

    class Meta:
        verbose_name = ("Testimony")
        verbose_name_plural = ("Testimonys")

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse("Testimony_detail", kwargs={"pk": self.pk})


