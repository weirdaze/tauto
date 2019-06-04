from django.db import models
from element.models import CodeRev
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.contenttypes.fields import GenericRelation
from django.shortcuts import reverse


class DeviceType(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inventory:device_type_view', args=[str(self.pk)])


class Serial(models.Model):
    number = models.CharField(max_length=300)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('inventory:serial_view', args=[str(self.pk)])


class ModelNo(models.Model):
    number = models.CharField(max_length=300)
    code = GenericRelation(CodeRev)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('inventory:model_view', args=[str(self.pk)])


class State(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=300)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inventory:state_view', args=[str(self.pk)])


class ModuleType(models.Model):
    name = models.CharField(max_length=300)
    model = GenericRelation(ModelNo)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inventory:module_type_view', args=[str(self.pk)])


class Speed(models.Model):
    speed = models.FloatField(default=0)
    unit = models.CharField(max_length=5, default='G')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()


class MacAddr(models.Model):
    address = models.CharField(max_length=100)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
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

    def get_absolute_url(self):
        return reverse('inventory:chip_type_view', args=[str(self.pk)])


class ChipModelNo(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inventory:chip_model_no_view', args=[str(self.pk)])


class SerdesType(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inventory:serdes_type_view', args=[str(self.pk)])


class SerdesSpeed(models.Model):
    speed = GenericRelation(Speed)


class Serdes(models.Model):
    name = models.CharField(max_length=300)
    speed = models.ForeignKey(SerdesSpeed, on_delete=models.CASCADE)
    type = models.ForeignKey(SerdesType, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class Chip(models.Model):
    name = models.CharField(max_length=300)
    serdes_num_front = models.PositiveIntegerField(default=0)
    serdes_num_fabric = models.PositiveIntegerField(default=0)
    serdes_speed_front = models.PositiveIntegerField(default=0)
    serdes_speed_fabric = models.PositiveIntegerField(default=0)
    serdes = GenericRelation(Serdes)
    model = models.ForeignKey(ChipModelNo, on_delete=models.CASCADE)
    macs = models.ManyToManyField(Mac)
    interface = GenericRelation(Interface)
    type = models.ForeignKey(ChipType, on_delete=models.DO_NOTHING, blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class ModuleBuildModelNo(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inventory:module_build_model_no_view', args=[str(self.pk)])


class ModuleBuildPorts(models.Model):
    name = models.CharField(max_length=300)
    num_phy_ports = models.PositiveIntegerField(default=0)
    speed_phy_ports = GenericRelation(Speed)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.name


class ModuleBuild(models.Model):
    name = models.CharField(max_length=300)
    fqdn = models.URLField(blank=True, null=True)
    chip = GenericRelation(Chip)
    model = models.ForeignKey(ModuleBuildModelNo, on_delete=models.CASCADE)
    ports = GenericRelation(ModuleBuildPorts)

    def __str__(self):
        return self.model


class ModuleSerial(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class ModuleState(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Module(models.Model):
    module_type = models.ForeignKey(ModuleType, on_delete=models.DO_NOTHING)
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=300, null=True, blank=True)
    slot = models.PositiveIntegerField(default=1)
    serial = models.ForeignKey(ModuleSerial, on_delete=models.CASCADE)
    module_build = models.ForeignKey(ModuleBuild, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(ModuleState, on_delete=models.DO_NOTHING)
    ip = GenericRelation(IPAddress)


class SlotModelNo(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inventory:slot_model_no_view', args=[str(self.pk)])


class SlotType(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inventory:slot_type_view', args=[str(self.pk)])


class Slot(models.Model):
    number = models.CharField(max_length=300)
    type = models.ForeignKey(SlotType, on_delete=models.CASCADE)
    module = GenericRelation(Module)
    model = models.ForeignKey(SlotModelNo, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class Link(models.Model):
    name = models.CharField(max_length=300)
    side_a = models.ForeignKey(Interface, on_delete=models.CASCADE, related_name='side_a')
    side_z = models.ForeignKey(Interface, on_delete=models.CASCADE, related_name='side_z')
    state = GenericRelation(State)
    tx_bandwidth_utilization = GenericRelation(BandwidthGigabits, related_name='tx_bandwidth_utilization')
    rx_bandwidth_utilization = GenericRelation(BandwidthGigabits, related_name='rx_bandwidth_utilization')


class DeviceModelNo(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inventory:device_model_no_view', args=[str(self.pk)])


class DeviceState(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class DeviceModel(models.Model):
    hostname = models.CharField(max_length=300)
    chassis = models.PositiveIntegerField(default=1)
    fqdn = models.URLField()
    serial = GenericRelation(Serial)
    mac = GenericRelation(MacAddr)
    model = models.ForeignKey(DeviceModelNo, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(DeviceState, on_delete=models.DO_NOTHING)
    slot = GenericRelation(Slot)
    num_slots = models.PositiveIntegerField(default=1)
    type = models.ForeignKey(DeviceType, on_delete=models.DO_NOTHING, blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.model.name


class Device(models.Model):
    hostname = models.CharField(max_length=300)
    chassis = models.PositiveIntegerField(default=1)
    fqdn = models.URLField()
    serial = GenericRelation(Serial)
    mac = GenericRelation(MacAddr)
    model = models.ForeignKey(DeviceModelNo, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(DeviceState, on_delete=models.DO_NOTHING)
    slot = GenericRelation(Slot)
    num_slots = models.PositiveIntegerField(default=1)
    type = models.ForeignKey(DeviceType, on_delete=models.DO_NOTHING, blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.fqdn
