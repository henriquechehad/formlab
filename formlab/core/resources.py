# -*- coding: utf-8 -*-

import os
import random
from datetime import datetime
from django.utils.text import slugify
from django.utils.deconstruct import deconstructible


@deconstructible
class FileUploadPath(object):
    def __init__(self, subfolder=None):
        self.subfolder = subfolder

    def __call__(self, instance, filename):
        filename = filename.replace(' ', '_')
        ext = filename.split('.')[-1]
        filename_without_ext = filename.split('.')[0]
        filename = u"{0}-{1}.{2}".format(
            slugify(filename_without_ext), random.getrandbits(32), ext)
        d = datetime.now()

        folder = u""

        if self.subfolder:
            folder += u"{sf}/{date}".format(
                sf=self.subfolder, date=d.strftime("%Y/%m/%d/"))
        else:
            folder = u"default/{date}".format(
                date=d.strftime("%Y/%m/%d/"))

        return os.path.join(folder, filename)
