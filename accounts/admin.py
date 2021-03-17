from django.contrib import admin

# Register your models here.
from .models import User, Profile, Review


admin.site.register(Profile)
admin.site.register(Review)

class UserAdmin(admin.ModelAdmin):
    list_display = ['email','password']
    # list_filter = ('email')
    search_fields = ['email']


admin.site.register(User, UserAdmin)