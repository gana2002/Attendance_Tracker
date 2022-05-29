from django.contrib import admin
from .models import Post, User
# Register your models here.
admin.site.register(Post)


admin.site.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email', 'password')