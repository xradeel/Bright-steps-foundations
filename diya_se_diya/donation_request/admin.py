from django.contrib import admin
from .models import d_request
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('new_title', 'new_image')


admin.site.register(d_request)