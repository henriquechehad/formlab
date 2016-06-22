# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False,
                                   verbose_name=u"Created date")
    last_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

from django.utils.text import slugify


class Slugged(models.Model):
    slug = models.SlugField(u"Slug", db_index=True, max_length=150)

    def generate_slug(self):
        if getattr(self, 'name', None):
            self.slug = slugify(self.name[:140])

        if getattr(self, 'title', None):
            self.slug = slugify(self.title[:140])

        filters = {'slug': self.slug}
        slug_exists = self.__class__.objects.filter(**filters)[:1]

        if slug_exists:
            count = self.__class__.objects.filter(
                slug__istartswith=self.slug + "-").count() + 1
            self.slug = "{}-{}".format(self.slug, count)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == "":
            self.generate_slug()
        super(Slugged, self).save(*args, **kwargs)

    class Meta:
        abstract = True
