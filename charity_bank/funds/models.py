from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="phone number must be in format +77771112233")


class Fund(models.Model):

    title = models.CharField(_('title'), max_length=128)
    info = models.CharField(_('info'), max_length=128)
    email = models.EmailField(_('email'), max_length=128)
    address = models.CharField(_('address'), max_length=128)
    logo = models.ImageField(_('logo'), upload_to='logos')
    phone = models.CharField(_('phone'), validators=[phone_regex], max_length=15, blank=True)

    def get_absolute_url(self):
        return reverse('fund-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


