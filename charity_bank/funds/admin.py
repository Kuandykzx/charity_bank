from .models import Fund
from django.contrib import admin
# Register your models here.


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = ('title',)


