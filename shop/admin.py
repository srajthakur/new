from django.contrib import admin

# Register your models here.
from .models import*
from import_export.admin import ImportExportModelAdmin
admin.site.register(product)
admin.site.register(contact)
admin.site.register(Cart)
admin.site.register(Login)
class PersonAdin(ImportExportModelAdmin):
    list_display=('loginid','loginname','password')