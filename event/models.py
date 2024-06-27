from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class OrganizeEvent(models.Model):
    EVENT_TYPES = [
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
        ('seminar', 'Seminar'),
        ('webinar', 'Webinar'),
        ('other', 'Other'),
    ]
    event_name = models.CharField(max_length= 50, null=False)
    event_data = models.DateField(null= False)
    event_description = models.TextField(max_length=1000, null=False)
    your_name = models.CharField(max_length=30, null=False)
    your_email = models.EmailField(null=False)
    your_phone = PhoneNumberField(null = False)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, null=False)
    event_time = models.TimeField(null=False)

    def __str__(self):
        return self.event_name

    