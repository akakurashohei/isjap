from django.contrib import admin
from .models import *

class DaemiInline(admin.TabularInline):
    model = Daemi

class DaemiOrdastaedaInline(admin.TabularInline):
    model = DaemiOrdastaeda

class OrdastaedaInline(admin.TabularInline):
    model = Ordastaeda

class JpJafnheitiInline(admin.TabularInline):
    model = JpJafnheiti

class FlettaAdmin(admin.ModelAdmin):
    fields = ['uppflettiord', 'ordmynd','ordflokkur', 'beygingarmynd', 'bin_id', 'ipa', 'upptaka','malsnid','efnisflokkur','buin']
    inlines = [JpJafnheitiInline, DaemiInline, OrdastaedaInline, DaemiOrdastaedaInline]
    list_filter = ['buin', 'ordflokkur', 'malsnid', 'efnisflokkur']
    search_fields = ['uppflettiord']
    list_display = ['id', 'uppflettiord', 'ordflokkur', 'buin', 'created_date']
    list_display_links = ['id', 'uppflettiord',]
    ordering = ['uppflettiord']

admin.site.register(Fletta, FlettaAdmin)
