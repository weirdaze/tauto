from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.


class DeviceType(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Serial(models.Model):
    number = models.CharField(max_length=300)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class ModelNo(models.Model):
    number = models.CharField(max_length=300)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class State(models.Model):
    name = models.CharField(max_length=300)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class ModuleType(models.Model):
    name = models.CharField(max_length=300)
    model = GenericRelation(ModelNo)


class Speed(models.Model):
    speed = models.FloatField(default=0)
    unit = models.CharField(max_length=5, default='G')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class MacAddr(models.Model):
    address = models.CharField(max_length=100)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class Mac(models.Model):
    speed = GenericRelation(Speed)


class BandwidthGigabits(models.Model):
    bw = models.FloatField(default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class IPAddress(models.Model):
    address = models.GenericIPAddressField(protocol='both')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class InterfaceType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Interface(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True, default='Interface Description')
    type = models.ForeignKey(InterfaceType, on_delete=models.DO_NOTHING)
    slot = models.PositiveIntegerField(default=1, null=True, blank=True)
    number = models.PositiveIntegerField(default=1)
    mac = GenericRelation(MacAddr)
    ip = GenericRelation(IPAddress, blank=True, null=True)
    speed = GenericRelation(Speed, blank=True, null=True)
    state = GenericRelation(State)
    verified = models.BooleanField(default=False)
    tx_bandwidth_utilization = GenericRelation(BandwidthGigabits,
                                               related_name='tx_bandwidth_utilization', blank=True, null=True)
    rx_bandwidth_utilization = GenericRelation(BandwidthGigabits,
                                               related_name='rx_bandwidth_utilization', blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class ChipType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Chip(models.Model):
    name = models.CharField(max_length=300)
    serdes_num_front = models.PositiveIntegerField(default=0)
    serdes_num_fabric = models.PositiveIntegerField(default=0)
    serdes_speed_front = models.PositiveIntegerField(default=0)
    serdes_speed_fabric = models.PositiveIntegerField(default=0)
    model = GenericRelation(ModelNo)
    macs = models.ManyToManyField(Mac)
    interface = GenericRelation(Interface)
    type = models.ForeignKey(ChipType, on_delete=models.DO_NOTHING, blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class ModuleBuild(models.Model):
    name = models.CharField(max_length=300)
    fqdn = models.URLField(blank=True, null=True)
    chip = GenericRelation(Chip)


class Module(models.Model):
    module_type = models.ForeignKey(ModuleType, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=300)
    chassis = models.PositiveIntegerField(default=1)
    slot = models.PositiveIntegerField(default=1)
    serial = GenericRelation(Serial)
    module_build = models.ForeignKey(ModuleBuild, on_delete=models.DO_NOTHING)
    state = GenericRelation(State)
    ip = GenericRelation(IPAddress, blank=True, null=True)


class Link(models.Model):
    name = models.CharField(max_length=300)
    side_a = models.ForeignKey(Interface, on_delete=models.CASCADE, related_name='side_a')
    side_z = models.ForeignKey(Interface, on_delete=models.CASCADE, related_name='side_z')
    state = GenericRelation(State)
    tx_bandwidth_utilization = GenericRelation(BandwidthGigabits, related_name='tx_bandwidth_utilization')
    rx_bandwidth_utilization = GenericRelation(BandwidthGigabits, related_name='rx_bandwidth_utilization')


class Device(models.Model):
    hostname = models.CharField(max_length=300)
    fqdn = models.URLField()
    serial = GenericRelation(Serial)
    mac = GenericRelation(MacAddr)
    model = GenericRelation(ModelNo)
    state = GenericRelation(State)
    module = GenericRelation(Module)
    num_slots = models.PositiveIntegerField(default=1)
    type = models.ForeignKey(DeviceType, on_delete=models.DO_NOTHING, blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.fqdn
