from django.contrib import admin
from django.contrib.auth.models import User,Group,Permission
from django.contrib.sessions.models import Session
from .models import agriculture,NPK
from agriproject.settings import BASE_DIR2
class myadmin(admin.AdminSite):
    list = ['state_name','district','n','p','k','temp','humidity','ph','rainfall','label',]
admin_site = myadmin()
admin_site.register(agriculture)
admin_site.register(NPK)
admin_site.register(User)
admin_site.register(Permission)
admin_site.register(Session)

# Register your models here.
