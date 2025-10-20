from django.contrib import admin
from .models import PYQ

@admin.register(PYQ)
class PYQAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'year', 'uploaded_by', 'created_at')
    search_fields = ('title', 'subject', 'year')
