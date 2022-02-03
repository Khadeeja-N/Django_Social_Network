from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Post


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    inlines = [ProfileInline]


# Unregister since user comes by default
admin.site.unregister(User)
# Re-register user
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)

admin.site.register(Post)
