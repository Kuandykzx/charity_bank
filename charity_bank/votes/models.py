from django.db import models

# Create your models here.


class Vote(models.Model):

    case = models.ForeignKey("cases.Case", on_delete=models.CASCADE, verbose_name='vote')
    number = models.IntegerField()

    def __str__(self):
        return self.case.header

