from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Comp

@admin.register(Comp)
class CompAdmin(ImportExportModelAdmin):
    pass