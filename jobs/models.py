from django.db import models
from django import forms
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/%Y/%m/%d/')
    url = models.CharField(max_length=300)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('CompanyDetailView', kwargs={'pk': self.pk})

RATING_CHOICES= [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
]

class CompanyReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='companies_reviewed',on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name = 'reviews', on_delete = models.CASCADE)
    star_rating = models.CharField(max_length = 10,choices=RATING_CHOICES)
    position = models.CharField(max_length=50)
    notes = models.TextField(max_length=600)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.company.name, self.user)

INTERVIEW_STAGE = [
    ('Applied','Applied'),
    ('Rejected', 'Rejected'),
    ('Online Assessment','Online Assessment'),
    ('1st Round Interview','1st Round Interview'),
    ('2nd Round Interview','2nd Round Interview'),
    ('3rd Round Intervew','3rd Round Intervew'),
    ('4th Round Interview','4th Round Interview'),
    ('Given Offer','Given Offer'),
]

class JobApplication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='jobs_applied',on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    stage = models.CharField(max_length=19, choices=INTERVIEW_STAGE)
    date_applied = models.DateField(default=timezone.now)





