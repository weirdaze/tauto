from django import forms
from .models import DeviceType, SlotType, ModuleType, ChipType, DeviceModelNo, SlotModelNo, ModuleBuildModelNo, ChipModelNo, SerdesType


class DeviceTypeForm(forms.ModelForm):
    class Meta:
        model = DeviceType
        fields = ['name']


class SerdesTypeForm(forms.ModelForm):
    class Meta:
        model = SerdesType
        fields = ['name']


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
        fields = ['name']
