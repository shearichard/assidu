from django.contrib import admin

admin.site.site_title = 'Assidu'
admin.site.site_header = 'Assidu Admin'
admin.site.index_title = 'Assidu Index'


# Register your models here.
from django.contrib import admin
from accounts.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
