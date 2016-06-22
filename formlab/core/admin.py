# -*- coding: UTF-8 -*-

from django.contrib import admin


class BaseStackedInline(admin.StackedInline):
    exclude = ["created", "last_modified", ]


class BaseTabularInline(admin.TabularInline):
    exclude = ["created", "last_modified", ]


class BaseAdmin(admin.ModelAdmin):
    exclude = ["created", "last_modified", ]
