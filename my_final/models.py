from django.db import models
from django.contrib.auth.models import User, AbstractUser


GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]

class BloodGroup(models.Model):
    name = models.CharField(max_length=5)
    
    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserExtend(models.Model):
    donor = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(help_text="yyyy-mm-dd")
    phone = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER, max_length=10)
    ready_to_donate = models.BooleanField(default=True)
    def __str__(self):
        return self.donor.username

class RequestBlood(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    donation_location = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    date_of_donation = models.DateField(help_text="yyyy-mm-dd")
    pin_code = models.IntegerField(help_text='Pin code for editing request later', unique=True)

    def __str__(self):
        return self.name

class UserExtend2(models.Model):
  
    patient = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    date_of_birth = models.DateField(help_text="yyyy-mm-dd")
    phone = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER, max_length=10)
    need_donation = models.BooleanField(default=True)
    def __str__(self):
        return self.patient.username