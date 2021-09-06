from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from typing import Set


admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    actions = [
        'activate_users',
    ]

    def activate_users(self, request,queryset):
        cnt = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, f'Activated {cnt} users.')
    activate_users.short_description = 'Activate Users'

def get_actions(self, request):
    actions = super().get_actions(request)
    if not request.user.has_perm('auth.change_user'):
        del actions['activate_users']
    return actions