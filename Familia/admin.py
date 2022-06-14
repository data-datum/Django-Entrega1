from django.contrib import admin

# Register your models here.

from .models  import Persona

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'fecha')

admin.site.register(Persona, PersonaAdmin)