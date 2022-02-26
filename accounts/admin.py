from django.contrib import admin
from accounts.models import User, LoginLog


class UserAdminView(admin.ModelAdmin):
    list_display = (
        'username', 'first_name',
        'last_name',
        'email', 'is_superuser',
        'is_active', 'date_joined',
        'last_login'
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('last_login', 'date_joined')


class LoginLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_login')
    search_fields = ('user',)


# Register your models here.
admin.site.register(User, UserAdminView)
admin.site.register(LoginLog, LoginLogAdmin)
