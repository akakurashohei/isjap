from django.contrib import admin
from .models import HafaSamband

# Register your models here.
class HafaSambandAdmin(admin.ModelAdmin):
    list_display = ['id', 'lemma', 'subject', 'name', 'email', 'create_date']
    list_display_links = ['id', 'lemma',  'subject']
    search_fields = ['id', 'name', 'email', 'lemma', 'sjubect', 'create_date']
    list_per_page = 25

admin.site.register(HafaSamband, HafaSambandAdmin)
