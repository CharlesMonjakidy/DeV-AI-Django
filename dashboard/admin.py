from django.contrib import admin
from .models import Analysis

@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ("user", "resultat", "created_at")
    list_filter = ("resultat", "created_at")
    search_fields = ("user__email",)
