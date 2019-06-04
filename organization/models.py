from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.contenttypes.fields import GenericRelation


class OrgRole(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class OrgMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(OrgRole, on_delete=models.DO_NOTHING)
    # there will be other attributes for this later

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


# Create your models here.
class OrgType(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey(OrgType, on_delete=models.CASCADE)
    leader = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    member = GenericRelation(OrgMember)

    def __str__(self):
        return self.name
