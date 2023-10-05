from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

from .models import Transaction, User

class UserAdminConfig(UserAdmin):
    ordering = ('-name',)
    list_filter = ('email', 'name', 'annual_income', 'aadhar_id', 'is_active', 'is_staff')
    search_fields = ('email', 'name', 'annual_income', 'aadhar_id')
    list_display = ('email', 'name', 'annual_income', 'aadhar_id', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'name', 'annual_income', 'aadhar_id')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    formfield_overrides = {
        User.annual_income: {'widget': Textarea(attrs={'rows': 1, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'annual_income', 'aadhar_id', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(Transaction)
admin.site.register(User, UserAdminConfig)
