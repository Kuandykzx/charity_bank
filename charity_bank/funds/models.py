from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="phone number must be in format +77771112233")


class Fund(models.Model):

    title = models.CharField(max_length=128)
    info = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    address = models.CharField(max_length=128)
    logo = models.ImageField(upload_to='logos')
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True)

    def get_absolute_url(self):
        return reverse('fund-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


