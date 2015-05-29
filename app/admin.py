from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from app.models import Word, User, WordCategory


class WordCategoryAdmin(admin.TabularInline):
    model = WordCategory
    fk_name = 'word'


class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'word_class', 'date_modified')
    list_filter = ('word_class', 'show_top', 'show_main')
    inlines = (WordCategoryAdmin, )


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Word, WordAdmin)
admin.site.register(User, UserAdmin)

admin.site.unregister(Site)
admin.site.unregister(Group)
