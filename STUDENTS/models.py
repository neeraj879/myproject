from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
# Create your models here.
class STUDENTS(models.Model):
     GENDER = [('male', 'Male'),('female', 'Female')]
     registration_number=models.CharField(max_length=200, unique=True)
     surname = models.CharField(max_length=200)
     firstname = models.CharField(max_length=200)
     middle_name = models.CharField(max_length=200, blank=True)
     gender = models.CharField(max_length=10, choices=GENDER, default='male')
     date_of_birth = models.DateField(default=timezone.now)
     date_of_admission = models.DateField(default=timezone.now)
     mobile_num_regex = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
     address = models.TextField(blank=True)
     
     def __str__(self):
         return f'{self.surname} {self.firstname} {self.middle_name} ({self.registration_number})'
    #def get_absolute_url(self):
    #    return reverse('student-detail', kwargs={'pk': self.pk})