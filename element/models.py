from django.db import models
from django.contrib.auth.models import User
import datetime
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class TimelineType(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Timeline(models.Model):
    name = models.CharField(max_length=300)
    type = models.ForeignKey(TimelineType, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    duration = models.DurationField(default=datetime.timedelta(days=10, hours=10, seconds=10), blank=True, null=True)
    date_due = models.DateTimeField(blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class CodeType(models.Model):
    # type will be EFT, GA, Maintenance, SWIX, RPM, etc.
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class OperatingSystem(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CodeRev(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200, blank=True, null=True)
    operating_system = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)
    suffix = models.CharField(max_length=20, blank=True, null=True)
    type = models.ForeignKey(CodeType, on_delete=models.CASCADE, blank=True, null=True)
    timeline = GenericRelation(Timeline)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    code = GenericRelation(CodeRev)

    def __str__(self):
        return self.name


class MethodType(models.Model):
    # this will be methods like SNMP, SSH-CLI, NETCONF, etc
    name = models.CharField(max_length=200)


class DataPointMethod(models.Model):
    name = models.CharField(max_length=200)
    code = GenericRelation(CodeRev)
    type = models.ForeignKey(MethodType, on_delete=models.CASCADE)
    script = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()


class DataChild(models.Model):
    name = models.CharField(max_length=200)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.name


class DataModel(models.Model):
    name = models.CharField(max_length=200)
    data_child = GenericRelation(DataChild)

    def __str__(self):
        return self.name


class DataPointCategory(models.Model):
    name = models.CharField(max_length=200)
    category = GenericRelation(DataChild)

    def __str__(self):
        return self.name


class DataPoint(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = GenericRelation(DataPointCategory)
    method = GenericRelation(DataPointMethod)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
