from django.contrib import admin
from .models import users
from .models import askforhelp
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'phone')


admin.site.register(users)
class BookAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'uniName', 'email', 'phone', 'address', 'city', 'state', 'requirement', 'detailsReq', 'capability', 'anythingelse')

admin.site.register(askforhelp)