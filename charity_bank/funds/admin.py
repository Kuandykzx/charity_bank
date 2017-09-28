from .models import Fund
from django.contrib import admin


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = ('title',)


