from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(MOTHER)
admin.site.register(CHILD1)
admin.site.register(PROFILE)

admin.site.site_header = 'JOHN MUIA'

