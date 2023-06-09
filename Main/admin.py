from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import Header,Email,Social,HomeInfo,Research,ResearchInterest,Graduate,Publication,Experience,ExperienceDetail,Photos,Footer,Project

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ["name","email","subject","created"]
    readonly_fields = ["name","email","subject","message"]

admin.site.register(Header)
admin.site.register(Social)
admin.site.register(Project)
admin.site.register(HomeInfo)
admin.site.register(Research)
admin.site.register(ResearchInterest)
admin.site.register(Graduate)
admin.site.register(Publication)
admin.site.register(Experience)
admin.site.register(ExperienceDetail)
admin.site.register(Photos)
admin.site.register(Footer)

admin.site.unregister(User)
admin.site.unregister(Group)