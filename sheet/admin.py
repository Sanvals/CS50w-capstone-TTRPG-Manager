from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import User, Character, Item, Spell, Feat, CharacterItem

# Register your models here.
admin.site.register(User)
admin.site.register(Character)
admin.site.register(Feat)
admin.site.register(CharacterItem)

class siteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Item, siteAdmin)
admin.site.register(Spell, siteAdmin)