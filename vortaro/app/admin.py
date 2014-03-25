from adminsortable.admin import SortableAdminMixin
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from vortaro.app.models import Word, Category, User


class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'word_class', 'order')
    list_editable = ('order',)
    list_filter = ('category', 'word_class')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Word, WordAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)

admin.site.unregister(Site)
admin.site.unregister(Group)
