from django.contrib import admin

from enterprises.models import Enterprise, EnterpriseMember


admin.site.register(Enterprise, admin.ModelAdmin)
admin.site.register(EnterpriseMember, admin.ModelAdmin)
