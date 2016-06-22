# -*- coding: utf-8 -*-

from pyxform.xls2xform import xls2xform_convert
from django.core.files import File
from django.conf import settings

import random


# @receiver(post_save, sender=Form)
def generate_xlsform(instance, created=False):
    """ Generate XLSForm file """
    output_file = "/tmp/{}-{}.xml".format(
        random.getrandbits(32), instance.pk)

    xls_filepath = "{}{}".format(settings.PROJECT_PATH, instance.xls_file.url)
    xls2xform_convert(xls_filepath, output_file)
    xlsform_file = File(open(output_file))

    filename = "{}.xml".format(instance.xls_file.name)
    instance.xlsform_file.save(filename, xlsform_file)
