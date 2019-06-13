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
        return reverse('device_model:device_type_view', args=[str(self.pk)])


class Serial(models.Model):
    number = models.CharField(max_length=300)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('device_model:serial_view', args=[str(self.pk)])


class ModelNo(models.Model):
    number = models.CharField(max_length=300)
    code = GenericRelation(CodeRev)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('device_model:model_view', args=[str(self.pk)])


class State(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=300)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('device_model:state_view', args=[str(self.pk)])


class ModuleType(models.Model):
    name = models.CharField(max_length=300)
    model = GenericRelation(ModelNo)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('device_model:module_type_view', args=[str(self.pk)])


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
    speed = models.PositiveIntegerField(default=0)
    unit = models.CharField(default='G', max_length=20)

    def __str__(self):
        return str(self.speed)+self.unit

    def get_absolute_url(self):
        return reverse('device_model:mac_view', args=[str(self.pk)])


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
        return reverse('device_model:chip_type_view', args=[str(self.pk)])


class ChipModelNo(models.Model):
    name = models.CharField(max_length=300)
    code_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " (" + self.code_name + ")"

    def get_absolute_url(self):
        return reverse('device_model:chip_model_no_view', args=[str(self.pk)])


class SerdesType(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('device_model:serdes_type_view', args=[str(self.pk)])


class SerdesSpeed(models.Model):
    speed = models.PositiveIntegerField(default=0)
    unit = models.CharField(default='G', max_length=20)

    def __str__(self):
        return str(self.speed) + self.unit

    def get_absolute_url(self):
        return reverse('device_model:serdes_speed_view', args=[str(self.pk)])


class Serdes(models.Model):
    name = models.CharField(max_length=300)
    speed = models.ForeignKey(SerdesSpeed, on_delete=models.CASCADE)
    type = models.ForeignKey(SerdesType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + str(self.speed)

    def get_absolute_url(self):
        return reverse('device_model:serdes_view', args=[str(self.pk)])


class Chip(models.Model):
    name = models.CharField(max_length=300)
    model = models.ForeignKey(ChipModelNo, on_delete=models.CASCADE)
    macs = models.ManyToManyField(Mac)
    type = models.ForeignKey(ChipType, on_delete=models.DO_NOTHING, blank=True, null=True)
    nif_serdes_num = models.PositiveIntegerField(default=0, blank=True, null=True)
    nif_serdes = models.ForeignKey(Serdes, on_delete=models.DO_NOTHING, related_name='nif_serdes', blank=True, null=True)
    fif_serdes_num = models.PositiveIntegerField(default=0, blank=True, null=True)
    fif_serdes = models.ForeignKey(Serdes, on_delete=models.DO_NOTHING, related_name='fif_serdes', blank=True, null=True)

    def __str__(self):
        return str(self.model)

    def get_absolute_url(self):
        return reverse('device_model:chip_view', args=[str(self.pk)])


class ModuleBuildModelNo(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('device_model:module_build_model_no_view', args=[str(self.pk)])


class ModuleBuild(models.Model):
    name = models.CharField(max_length=300)
    fqdn = models.URLField(blank=True, null=True)
    model = models.ForeignKey(ModuleBuildModelNo, on_delete=models.CASCADE)
    ports = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.model.name

    def get_absolute_url(self):
        return reverse('device_model:module_build_view', args=[str(self.pk)])


class ChipModel(models.Model):
    chip = models.ForeignKey(Chip, on_delete=models.CASCADE, blank=True, null=True)
    interface = GenericRelation(Interface)
    module_build = models.ForeignKey(ModuleBuild, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.chip.model.code_name + " (" + self.module_build.model.name + ")"

    def get_absolute_url(self):
        return reverse('device_model:chip_model_view', args=[str(self.pk)])


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
        return reverse('device_model:slot_model_no_view', args=[str(self.pk)])


class SlotType(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('device_model:slot_type_view', args=[str(self.pk)])


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
        return reverse('device_model:device_model_no_view', args=[str(self.pk)])


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
