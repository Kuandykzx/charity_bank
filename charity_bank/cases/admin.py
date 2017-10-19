from django import forms
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Case, GalleryItem, ContentItem


class ContentItemAdminForm(forms.ModelForm):

    class Meta:
        model = ContentItem
        widgets = {
            'list': forms.Textarea
        }
        fields = '__all__'


class ContentItemInlineAdmin(admin.StackedInline):
    model = ContentItem
    extra = 0


class GalleryItemInlineAdmin(admin.StackedInline):
    model = GalleryItem
    extra = 0


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    inlines = [ContentItemInlineAdmin]
    list_display = ('title', 'fund')


@admin.register(ContentItem)
class ContentItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = ContentItemAdminForm
    inlines = [GalleryItemInlineAdmin]
    list_display = ('header', 'case',)
    list_filter = ('case__title',)
