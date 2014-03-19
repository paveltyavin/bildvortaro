from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from vortaro.app.models import Word, Category


class WordAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Word, WordAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.unregister(Site)
admin.site.unregister(Group)
