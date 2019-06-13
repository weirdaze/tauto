from django import forms
from .models import DeviceType, SlotType, ModuleType, ChipType, DeviceModelNo, SlotModelNo, ModuleBuildModelNo, ChipModelNo, SerdesType, SerdesSpeed, Mac, Chip, Serdes, ModuleBuild, ChipModel


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


class SerdesForm(forms.ModelForm):
    class Meta:
        model = Serdes
        fields = ['name', 'speed', 'type']


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


class ModuleBuildForm(forms.ModelForm):
    class Meta:
        model = ModuleBuild
        fields = ['name', 'model', 'ports']


class ChipModelNoForm(forms.ModelForm):
    class Meta:
        model = ChipModelNo
        fields = ['name', 'code_name']


class ChipForm(forms.ModelForm):
    class Meta:
        model = Chip
        fields = ['name', 'model', 'type', 'macs', 'nif_serdes_num', 'nif_serdes', 'fif_serdes_num', 'fif_serdes']


class ChipModelForm(forms.ModelForm):
    class Meta:
        model = ChipModel
        fields = ['chip', 'module_build']


class ChipModelModuleBuildForm(forms.ModelForm):
    qty = forms.IntegerField(required=True)

    class Meta:
        model = ChipModel
        fields = ['chip']