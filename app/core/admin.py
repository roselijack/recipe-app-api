from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
# 自定义admin时，继承与from django.contrib.auth.admin import UserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    # 继承于BaseUserAdmin，但更改一些fields.
    # 问题：子类和父类的类名可以一致？
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
# register class UserAdmin到model User
