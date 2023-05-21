from django.contrib import admin
from . import models
# Register your models here.
# to make the GroupMember in side of Group model use this class


class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)
