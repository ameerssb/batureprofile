from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Post,Department,Footer,Email,Contact,About

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    exclude = ('user',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

class DepartmentAdmin(admin.ModelAdmin):
    exclude = ('user',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

class FooterAdmin(admin.ModelAdmin):
    exclude = ('user',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

class ContactAdmin(admin.ModelAdmin):
    exclude = ('user',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

class AboutAdmin(admin.ModelAdmin):
    exclude = ('user',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(User,UserAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Footer,FooterAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Email)