from django.contrib import  admin
from vortaro.app.models import Word


class WordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Word, WordAdmin)