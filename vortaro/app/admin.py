from adminsortable.admin import SortableAdminMixin
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from vortaro.app.models import Word, User


class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'word_class', 'order', 'date_modified')
    list_editable = ('order',)
    list_filter = ('word_class', 'show_top', 'show_main')


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Word, WordAdmin)
admin.site.register(User, UserAdmin)

admin.site.unregister(Site)
admin.site.unregister(Group)
