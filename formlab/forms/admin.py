# -*- coding: UTF-8 -*-

from django.contrib import admin
from .models import Form
from formlab.core.admin import BaseAdmin


@admin.register(Form)
class FormAdmin(BaseAdmin):
    readonly_fields = [
        "created", "last_modified", "xlsform_file", "slug", "owner", ]
    list_display = ["title", "created", "last_modified"]
    fields = [
        "owner", "slug", "title", "xls_file", "xlsform_file",
        "groups", "description", "created", "last_modified",
    ]

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()
