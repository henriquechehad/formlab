# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.db import models
from formlab.core.models import BaseModel, Slugged
from formlab.core.resources import FileUploadPath


xlsfiles_path = FileUploadPath('xlsfiles')
xlsforms_path = FileUploadPath('xlsforms')


class Form(BaseModel, Slugged):
    title = models.CharField(max_length=150, verbose_name=u"Title")
    owner = models.ForeignKey("auth.User", verbose_name=u"Owner")
    groups = models.ManyToManyField("auth.Group", null=True, blank=True,
                                    verbose_name=u"User Groups")
    description = models.TextField(null=True, blank=True,
                                   verbose_name=u"Description")
    xls_file = models.FileField(upload_to=xlsfiles_path, max_length=255,
                                verbose_name=u"XLS File")
    xlsform_file = models.FileField(upload_to=xlsforms_path, max_length=255,
                                    verbose_name=u"XLSForm File",
                                    null=True, blank=True)

    class Meta:
        verbose_name = u"Form"
        verbose_name_plural = u"Forms"

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Form, self).save(*args, **kwargs)
        if not self.xlsform_file:
            from .resources import generate_xlsform
            generate_xlsform(self)

        super(Form, self).save(*args, **kwargs)
