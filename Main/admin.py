from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import Social,HomeInfo,Research,ResearchInterest,Graduate,Publication,Experience,ExperienceDetail,Photos,Footer,Project

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