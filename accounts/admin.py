from django.contrib import admin
from django.utils import timezone
from .models import Profile

@admin.action(description="Approuver les utilisateurs sélectionnés")
def approve_users(modeladmin, request, queryset):
    queryset.update(status="approved", approved_at=timezone.now())

@admin.action(description="Refuser les utilisateurs sélectionnés")
def reject_users(modeladmin, request, queryset):
    queryset.update(status="rejected")

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "status", "approved_at")
    list_filter = ("status",)
    search_fields = ("user__email", "user__username")
    actions = [approve_users, reject_users]
