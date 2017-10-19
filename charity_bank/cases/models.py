from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _

import re

GALLERY_TYPE_CHOICES = (
    ('carousel', 'carousel'),
    ('slide', 'slide'),
    ('video', 'video'),
)


class Category(models.Model):
    name = models.CharField(_('name'), max_length=128)


class Case(models.Model):
    title = models.CharField(_('title'), max_length=128, default="")
    sub_header = models.CharField(_('sub_header'), max_length=256, blank=True, null=True)
    fund = models.ForeignKey("funds.Fund", on_delete=models.CASCADE, verbose_name='fund')

    required_sum = models.IntegerField(_("required sum"))
    is_active = models.BooleanField(_('is active'), default=True)
    video = models.URLField(_('video'), max_length=256, null=True)
    bg_photo = models.ImageField(_('image'))

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.id})

    @property
    def youtube_embed_url(self):
        match = re.search(r'^(http|https)\:\/\/www\.youtube\.com\/watch\?v\=(\w*)(\&(.*))?$', self.video)
        if match:
            embed_url = 'http://www.youtube.com/embed/%s' % (match.group(2))
            return embed_url
        return self.video

    def __str__(self):
        return self.title


class ContentItem(models.Model):

    header = models.CharField(_('header'), max_length=64)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, verbose_name='case')

    text_1 = models.TextField(_('text'), blank=True, null=True)
    list = ArrayField(models.TextField(), size=16, null=True, blank=True)
    accent = models.TextField(_('accent'), blank=True, null=True)
    text_after_item = models.TextField(_('text'), blank=True, null=True)

    type = models.CharField(_('type'), max_length=8, choices=GALLERY_TYPE_CHOICES, blank=True, null=True)
    #  image = models.ImageField(_('image'), null=True, blank=True)
    video = models.URLField(_('video'), max_length=256, null=True, blank=True)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.header

    class Meta:
        ordering = ['order']


class GalleryItem(models.Model):

    #title = models.CharField(_('title'), max_length=128)
    image = models.ImageField(_('image'), null=True, blank=True)
    content_item = models.ForeignKey(ContentItem, on_delete=models.CASCADE, verbose_name='content item')

    def __str__(self):
        return self.content_item.header

