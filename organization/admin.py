from django.contrib import admin
from .models import OrgType, Organization, OrgRole, OrgMember


# Register your models here.
admin.site.register(OrgType)
admin.site.register(Organization)
admin.site.register(OrgRole)
admin.site.register(OrgMember)
