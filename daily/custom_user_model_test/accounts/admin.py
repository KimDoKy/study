from django.contrib import admin
from .models import CustomUser, CompCategory

class CustomAdmin(admin.ModelAdmin):
    fields = ('nick_name', 'comp_cate', 'username')

class GroupInline(admin.StackedInline):
    model = CustomUser.comp_cate.through
    extra = 3

class GroupAdmin(admin.ModelAdmin):
    inlines = [
            GroupInline,
            ]
    exclude = ('comp_cate',)
    fields = ('cate_name', 'cate_name_2')

admin.site.register(CustomUser, CustomAdmin)
admin.site.register(CompCategory, GroupAdmin)
