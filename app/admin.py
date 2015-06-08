from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from app.models import Word, User


class WordAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date_modified',
    )


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Word, WordAdmin)
admin.site.register(User, UserAdmin)

admin.site.unregister(Site)
admin.site.unregister(Group)
