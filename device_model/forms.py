from django import forms
from .models import DeviceType, SlotType, ModuleType, ChipType, DeviceModelNo, SlotModelNo, ModuleBuildModelNo, ChipModelNo, SerdesType, SerdesSpeed, Mac, Chip


class DeviceTypeForm(forms.ModelForm):
    class Meta:
        model = DeviceType
        fields = ['name']


class SerdesTypeForm(forms.ModelForm):
    class Meta:
        model = SerdesType
        fields = ['name']


class SerdesSpeedForm(forms.ModelForm):
    class Meta:
        model = SerdesSpeed
        fields = ['speed', 'unit']


class MacForm(forms.ModelForm):
    class Meta:
        model = Mac
        fields = ['speed', 'unit']


class SlotTypeForm(forms.ModelForm):
    class Meta:
        model = SlotType
        fields = ['name']


class ModuleTypeForm(forms.ModelForm):
    class Meta:
        model = ModuleType
        fields = ['name']


class ChipTypeForm(forms.ModelForm):
    class Meta:
        model = ChipType
        fields = ['name']


class DeviceModelNoForm(forms.ModelForm):
    class Meta:
        model = DeviceModelNo
        fields = ['name']


class SlotModelNoForm(forms.ModelForm):
    class Meta:
        model = SlotModelNo
        fields = ['name']


class ModuleBuildModelNoForm(forms.ModelForm):
    class Meta:
        model = ModuleBuildModelNo
        fields = ['name']


class ChipModelNoForm(forms.ModelForm):
    class Meta:
        model = ChipModelNo
        fields = ['name', 'code_name']


class ChipForm(forms.ModelForm):
    class Meta:
        model = Chip
        fields = ['name', 'model', 'type', 'macs']
