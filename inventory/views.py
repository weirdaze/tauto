from __future__ import absolute_import, unicode_literals
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy

from .models import DeviceType, SlotType, ModuleType, ChipType, DeviceModelNo, SlotModelNo, ModuleBuildModelNo, ChipModelNo, SerdesType
from .forms import DeviceTypeForm, SlotTypeForm, ModuleTypeForm, ChipTypeForm, DeviceModelNoForm, SlotModelNoForm, ModuleBuildModelNoForm, ChipModelNoForm, SerdesTypeForm


# Create your views here.

# --------------------------------------------
# Device Type CRUD
# --------------------------------------------
# Create your views here.
class DeviceTypeListView(ListView):
    model = DeviceType
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("device types", "/inventory/device_type_list/"),
        ("device type list", "/inventory/device_type_list")
    ]

    extra_context = {
        'breadcrumb_title': 'Device Type',
        'section_title': 'Device Types',
        'breadcrumb_path': path,
        'create': 'inventory:device_type_create',
        'delete': 'inventory:device_type_delete',
        'update': 'inventory:device_type_update',
        'cancel': 'inventory:device_type_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(DeviceTypeListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_queryset(self):
        queryset = DeviceType.objects.all()
        return queryset


class DeviceTypeUpdateView(UpdateView):
    model = DeviceType
    form_class = DeviceTypeForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("device types", '/inventory/device_type_list'),
        ("device type update", "/inventory/device_type_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Device Type Update',
        'section_title': 'Device Type Update',
        'breadcrumb_path': path,
        'create': 'inventory:device_type_create',
        'delete': 'inventory:device_type_delete',
        'update': 'inventory:device_type_update',
        'cancel': 'inventory:device_type_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(DeviceTypeUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class DeviceTypeCreateView(CreateView):
    model = DeviceType
    form_class = DeviceTypeForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("device types", '/inventory/device_type_list'),
        ("device type create", "/inventory/device_type_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Device Type Create',
        'section_title': 'Device Type Create',
        'breadcrumb_path': path,
        'create': 'inventory:device_type_create',
        'delete': 'inventory:device_type_delete',
        'update': 'inventory:device_type_update',
        'cancel': 'inventory:device_type_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(DeviceTypeCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class DeviceTypeDetailView(DetailView):
    model = DeviceType
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("device types", '/inventory/device_type_list'),
        ("device type detail", "/inventory/device_type_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Device Type Detail',
        'section_title': 'Device Type Detail',
        'breadcrumb_path': path,
        'create': 'inventory:device_type_create',
        'delete': 'inventory:device_type_delete',
        'update': 'inventory:device_type_update',
        'cancel': 'inventory:device_type_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(DeviceTypeDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    '''def get_queryset(self):
        queryset = Step.objects.get(pk=self.kwargs['pk'])
        return queryset'''


class DeviceTypeDeleteView(DeleteView):
    model = DeviceType
    success_url = reverse_lazy('inventory:device_type_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("device types", 'inventory/device_type_list'),
        ("device type delete", "/inventory/device_type_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Device Type Delete',
        'section_title': 'Device Type Delete',
        'breadcrumb_path': path,
        'create': 'inventory:device_type_create',
        'delete': 'inventory:device_type_delete',
        'update': 'inventory:device_type_update',
        'cancel': 'inventory:device_type_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(DeviceTypeDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


# --------------------------------------------
# SerDes Type CRUD
# --------------------------------------------
# Create your views here.
class SerdesTypeListView(ListView):
    model = SerdesType
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("serdes types", "/inventory/serdes_type_list/"),
        ("serdes type list", "/inventory/serdes_type_list")
    ]

    extra_context = {
        'breadcrumb_title': 'Serdes Type',
        'section_title': 'Serdes Types',
        'breadcrumb_path': path,
        'create': 'inventory:serdes_type_create',
        'delete': 'inventory:serdes_type_delete',
        'update': 'inventory:serdes_type_update',
        'cancel': 'inventory:serdes_type_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(SerdesTypeListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_queryset(self):
        queryset = SerdesType.objects.all()
        return queryset


class SerdesTypeUpdateView(UpdateView):
    model = SerdesType
    form_class = SerdesTypeForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("serdes types", '/inventory/serdes_type_list'),
        ("serdes type update", "/inventory/serdes_type_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Serdes Type Update',
        'section_title': 'Serdes Type Update',
        'breadcrumb_path': path,
        'create': 'inventory:serdes_type_create',
        'delete': 'inventory:serdes_type_delete',
        'update': 'inventory:serdes_type_update',
        'cancel': 'inventory:serdes_type_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(SerdesTypeUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class SerdesTypeCreateView(CreateView):
    model = SerdesType
    form_class = SerdesTypeForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("serdes types", '/inventory/serdes_type_list'),
        ("serdes type create", "/inventory/serdes_type_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Serdes Type Create',
        'section_title': 'Serdes Type Create',
        'breadcrumb_path': path,
        'create': 'inventory:serdes_type_create',
        'delete': 'inventory:serdes_type_delete',
        'update': 'inventory:serdes_type_update',
        'cancel': 'inventory:serdes_type_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(SerdesTypeCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class SerdesTypeDetailView(DetailView):
    model = SerdesType
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("serdes types", '/inventory/serdes_type_list'),
        ("serdes type detail", "/inventory/serdes_type_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Serdes Type Detail',
        'section_title': 'Serdes Type Detail',
        'breadcrumb_path': path,
        'create': 'inventory:serdes_type_create',
        'delete': 'inventory:serdes_type_delete',
        'update': 'inventory:serdes_type_update',
        'cancel': 'inventory:serdes_type_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(SerdesTypeDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class SerdesTypeDeleteView(DeleteView):
    model = SerdesType
    success_url = reverse_lazy('inventory:serdes_type_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("serdes types", 'inventory/serdes_type_list'),
        ("serdes type delete", "/inventory/serdes_type_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Serdes Type Delete',
        'section_title': 'Serdes Type Delete',
        'breadcrumb_path': path,
        'create': 'inventory:serdes_type_create',
        'delete': 'inventory:serdes_type_delete',
        'update': 'inventory:serdes_type_update',
        'cancel': 'inventory:serdes_type_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(SerdesTypeDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


# --------------------------------------------
# Slot Type CRUD
# --------------------------------------------
# Create your views here.
class SlotTypeListView(ListView):
    model = SlotType
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("slot types", "/inventory/slot_type_list/"),
        ("slot type list", "/inventory/slot_type_list")
    ]

    extra_context = {
        'breadcrumb_title': 'Slot Type',
        'section_title': 'Slot Types',
        'breadcrumb_path': path,
        'create': 'inventory:slot_type_create',
        'delete': 'inventory:slot_type_delete',
        'update': 'inventory:slot_type_update',
        'cancel': 'inventory:slot_type_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(SlotTypeListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_queryset(self):
        queryset = SlotType.objects.all()
        return queryset


class SlotTypeUpdateView(UpdateView):
    model = SlotType
    form_class = SlotTypeForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("slot types", '/inventory/slot_type_list'),
        ("slot type update", "/inventory/slot_type_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Slot Type Update',
        'section_title': 'Slot Type Update',
        'breadcrumb_path': path,
        'create': 'inventory:slot_type_create',
        'delete': 'inventory:slot_type_delete',
        'update': 'inventory:slot_type_update',
        'cancel': 'inventory:slot_type_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(SlotTypeUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class SlotTypeCreateView(CreateView):
    model = SlotType
    form_class = SlotTypeForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("slot types", '/inventory/slot_type_list'),
        ("slot type create", "/inventory/slot_type_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Slot Type Create',
        'section_title': 'Slot Type Create',
        'breadcrumb_path': path,
        'create': 'inventory:slot_type_create',
        'delete': 'inventory:slot_type_delete',
        'update': 'inventory:slot_type_update',
        'cancel': 'inventory:slot_type_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(SlotTypeCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class SlotTypeDetailView(DetailView):
    model = SlotType
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("slot types", '/inventory/slot_type_list'),
        ("slot type detail", "/inventory/slot_type_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Slot Type Detail',
        'section_title': 'Slot Type Detail',
        'breadcrumb_path': path,
        'create': 'inventory:slot_type_create',
        'delete': 'inventory:slot_type_delete',
        'update': 'inventory:slot_type_update',
        'cancel': 'inventory:slot_type_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(SlotTypeDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    '''def get_queryset(self):
        queryset = SlotType.objects.get(pk=self.kwargs['pk'])
        return queryset'''


class SlotTypeDeleteView(DeleteView):
    model = SlotType
    success_url = reverse_lazy('inventory:slot_type_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("device types", 'inventory/slot_type_list'),
        ("device type delete", "/inventory/slot_type_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Slot Type Delete',
        'section_title': 'Slot Type Delete',
        'breadcrumb_path': path,
        'create': 'inventory:slot_type_create',
        'delete': 'inventory:slot_type_delete',
        'update': 'inventory:slot_type_update',
        'cancel': 'inventory:slot_type_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(SlotTypeDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


# --------------------------------------------
# Module Type CRUD
# --------------------------------------------
# Create your views here.
class ModuleTypeListView(ListView):
    model = ModuleType
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("module types", "/inventory/module_type_list/"),
        ("module type list", "/inventory/module_type_list")
    ]

    extra_context = {
        'breadcrumb_title': 'Module Type',
        'section_title': 'Module Types',
        'breadcrumb_path': path,
        'create': 'inventory:module_type_create',
        'delete': 'inventory:module_type_delete',
        'update': 'inventory:module_type_update',
        'cancel': 'inventory:module_type_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(ModuleTypeListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_queryset(self):
        queryset = ModuleType.objects.all()
        return queryset


class ModuleTypeUpdateView(UpdateView):
    model = ModuleType
    form_class = ModuleTypeForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("module types", '/inventory/module_type_list'),
        ("module type update", "/inventory/module_type_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Module Type Update',
        'section_title': 'Module Type Update',
        'breadcrumb_path': path,
        'create': 'inventory:module_type_create',
        'delete': 'inventory:module_type_delete',
        'update': 'inventory:module_type_update',
        'cancel': 'inventory:module_type_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(ModuleTypeUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class ModuleTypeCreateView(CreateView):
    model = ModuleType
    form_class = ModuleTypeForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("module types", '/inventory/module_type_list'),
        ("module type create", "/inventory/module_type_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Module Type Create',
        'section_title': 'Module Type Create',
        'breadcrumb_path': path,
        'create': 'inventory:module_type_create',
        'delete': 'inventory:module_type_delete',
        'update': 'inventory:module_type_update',
        'cancel': 'inventory:module_type_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(ModuleTypeCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class ModuleTypeDetailView(DetailView):
    model = ModuleType
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("module types", '/inventory/module_type_list'),
        ("module type detail", "/inventory/module_type_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Module Type Detail',
        'section_title': 'Module Type Detail',
        'breadcrumb_path': path,
        'create': 'inventory:module_type_create',
        'delete': 'inventory:module_type_delete',
        'update': 'inventory:module_type_update',
        'cancel': 'inventory:module_type_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(ModuleTypeDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class ModuleTypeDeleteView(DeleteView):
    model = ModuleType
    success_url = reverse_lazy('inventory:module_type_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("module types", 'inventory/module_type_list'),
        ("module type delete", "/inventory/module_type_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Module Type Delete',
        'section_title': 'Module Type Delete',
        'breadcrumb_path': path,
        'create': 'inventory:module_type_create',
        'delete': 'inventory:module_type_delete',
        'update': 'inventory:module_type_update',
        'cancel': 'inventory:module_type_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(ModuleTypeDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


# --------------------------------------------
# Chip Type CRUD
# --------------------------------------------
# Create your views here.
class ChipTypeListView(ListView):
    model = ChipType
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("chip types", "/inventory/chip_type_list/"),
        ("chip type list", "/inventory/chip_type_list")
    ]

    extra_context = {
        'breadcrumb_title': 'Chip Type',
        'section_title': 'Chip Types',
        'breadcrumb_path': path,
        'create': 'inventory:chip_type_create',
        'delete': 'inventory:chip_type_delete',
        'update': 'inventory:chip_type_update',
        'cancel': 'inventory:chip_type_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(ChipTypeListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_queryset(self):
        queryset = ChipType.objects.all()
        return queryset


class ChipTypeUpdateView(UpdateView):
    model = ChipType
    form_class = ChipTypeForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("chip types", '/inventory/chip_type_list'),
        ("chip type update", "/inventory/chip_type_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Chip Type Update',
        'section_title': 'Chip Type Update',
        'breadcrumb_path': path,
        'create': 'inventory:chip_type_create',
        'delete': 'inventory:chip_type_delete',
        'update': 'inventory:chip_type_update',
        'cancel': 'inventory:chip_type_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(ChipTypeUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class ChipTypeCreateView(CreateView):
    model = ChipType
    form_class = ChipTypeForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("chip types", '/inventory/chip_type_list'),
        ("chip type create", "/inventory/chip_type_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Chip Type Create',
        'section_title': 'Chip Type Create',
        'breadcrumb_path': path,
        'create': 'inventory:chip_type_create',
        'delete': 'inventory:chip_type_delete',
        'update': 'inventory:chip_type_update',
        'cancel': 'inventory:chip_type_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(ChipTypeCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class ChipTypeDetailView(DetailView):
    model = ChipType
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("chip types", '/inventory/chip_type_list'),
        ("chip type detail", "/inventory/chip_type_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Chip Type Detail',
        'section_title': 'Chip Type Detail',
        'breadcrumb_path': path,
        'create': 'inventory:chip_type_create',
        'delete': 'inventory:chip_type_delete',
        'update': 'inventory:chip_type_update',
        'cancel': 'inventory:chip_type_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(ChipTypeDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class ChipTypeDeleteView(DeleteView):
    model = ChipType
    success_url = reverse_lazy('inventory:chip_type_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("chip types", 'inventory/chip_type_list'),
        ("chip type delete", "/inventory/chip_type_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Chip Type Delete',
        'section_title': 'Chip Type Delete',
        'breadcrumb_path': path,
        'create': 'inventory:chip_type_create',
        'delete': 'inventory:chip_type_delete',
        'update': 'inventory:chip_type_update',
        'cancel': 'inventory:chip_type_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(ChipTypeDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


# -------------------------------------------------------------------------------------------------#
#                                     Model Numbers                                                #
# -------------------------------------------------------------------------------------------------#
# --------------------------------------------
# Device Model Number CRUD
# --------------------------------------------
# Create your views here.
class DeviceModelNoListView(ListView):
    model = DeviceModelNo
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("device model numbers", "/inventory/device_model_no_list/"),
        ("device model numbers list", "/inventory/device_model_no_list")
    ]

    extra_context = {
        'breadcrumb_title': 'Device Model Number',
        'section_title': 'Device Model Numbers',
        'breadcrumb_path': path,
        'create': 'inventory:device_model_no_create',
        'delete': 'inventory:device_model_no_delete',
        'update': 'inventory:device_model_no_update',
        'cancel': 'inventory:device_model_no_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(DeviceModelNoListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_queryset(self):
        queryset = DeviceModelNo.objects.all()
        return queryset


class DeviceModelNoUpdateView(UpdateView):
    model = DeviceModelNo
    form_class = DeviceModelNoForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("device model numbers", '/inventory/device_model_no_list'),
        ("device model number update", "/inventory/device_model_no_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Device Model Number Update',
        'section_title': 'Device Model Number Update',
        'breadcrumb_path': path,
        'create': 'inventory:device_model_no_create',
        'delete': 'inventory:device_model_no_delete',
        'update': 'inventory:device_model_no_update',
        'cancel': 'inventory:device_model_no_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(DeviceModelNoUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class DeviceModelNoCreateView(CreateView):
    model = DeviceModelNo
    form_class = DeviceModelNoForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("device model numbers", '/inventory/device_model_no_list'),
        ("device model number create", "/inventory/device_model_no_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Device Model Number Create',
        'section_title': 'Device Model Number Create',
        'breadcrumb_path': path,
        'create': 'inventory:device_model_no_create',
        'delete': 'inventory:device_model_no_delete',
        'update': 'inventory:device_model_no_update',
        'cancel': 'inventory:device_model_no_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(DeviceModelNoCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class DeviceModelNoDetailView(DetailView):
    model = DeviceModelNo
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("device model numbers", '/inventory/device_model_no_list'),
        ("device model number detail", "/inventory/device_model_no_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Device Model Number Detail',
        'section_title': 'Device Model Number Detail',
        'breadcrumb_path': path,
        'create': 'inventory:device_model_no_create',
        'delete': 'inventory:device_model_no_delete',
        'update': 'inventory:device_model_no_update',
        'cancel': 'inventory:device_model_no_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(DeviceModelNoDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class DeviceModelNoDeleteView(DeleteView):
    model = DeviceModelNo
    success_url = reverse_lazy('inventory:device_model_no_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("device model numbers", 'inventory/device_model_no_list'),
        ("device model number delete", "/inventory/device_model_no_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Device Model Number Delete',
        'section_title': 'Device Model Number Delete',
        'breadcrumb_path': path,
        'create': 'inventory:device_model_no_create',
        'delete': 'inventory:device_model_no_delete',
        'update': 'inventory:device_model_no_update',
        'cancel': 'inventory:device_model_no_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(DeviceModelNoDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


# --------------------------------------------
# Slot Model No CRUD
# --------------------------------------------
# Create your views here.
class SlotModelNoListView(ListView):
    model = SlotModelNo
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("slot model numbers", "/inventory/slot_model_no_list/"),
        ("slot model number list", "/inventory/slot_model_no_list")
    ]

    extra_context = {
        'breadcrumb_title': 'Slot Model Number',
        'section_title': 'Slot Model Numbers',
        'breadcrumb_path': path,
        'create': 'inventory:slot_model_no_create',
        'delete': 'inventory:slot_model_no_delete',
        'update': 'inventory:slot_model_no_update',
        'cancel': 'inventory:slot_model_no_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(SlotModelNoListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_queryset(self):
        queryset = SlotModelNo.objects.all()
        return queryset


class SlotModelNoUpdateView(UpdateView):
    model = SlotModelNo
    form_class = SlotModelNoForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("slot model numbers", '/inventory/slot_model_no_list'),
        ("slot model number update", "/inventory/slot_model_no_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Slot Model Number Update',
        'section_title': 'Slot Model Number Update',
        'breadcrumb_path': path,
        'create': 'inventory:slot_model_no_create',
        'delete': 'inventory:slot_model_no_delete',
        'update': 'inventory:slot_model_no_update',
        'cancel': 'inventory:slot_model_no_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(SlotModelNoUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class SlotModelNoCreateView(CreateView):
    model = SlotModelNo
    form_class = SlotModelNoForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("slot model numbers", '/inventory/slot_model_no_list'),
        ("slot model number create", "/inventory/slot_model_no_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Slot Model Number Create',
        'section_title': 'Slot Model Number Create',
        'breadcrumb_path': path,
        'create': 'inventory:slot_model_no_create',
        'delete': 'inventory:slot_model_no_delete',
        'update': 'inventory:slot_model_no_update',
        'cancel': 'inventory:slot_model_no_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(SlotModelNoCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class SlotModelNoDetailView(DetailView):
    model = SlotModelNo
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("slot model numbers", '/inventory/slot_model_no_list'),
        ("slot model number detail", "/inventory/slot_model_no_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Slot Model Number Detail',
        'section_title': 'Slot Model Number Detail',
        'breadcrumb_path': path,
        'create': 'inventory:slot_model_no_create',
        'delete': 'inventory:slot_model_no_delete',
        'update': 'inventory:slot_model_no_update',
        'cancel': 'inventory:slot_model_no_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(SlotModelNoDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class SlotModelNoDeleteView(DeleteView):
    model = SlotModelNo
    success_url = reverse_lazy('inventory:slot_model_no_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("device model numbers", 'inventory/slot_model_no_list'),
        ("device model numbers delete", "/inventory/slot_model_no_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Slot Model Number Delete',
        'section_title': 'Slot Model Number Delete',
        'breadcrumb_path': path,
        'create': 'inventory:slot_model_no_create',
        'delete': 'inventory:slot_model_no_delete',
        'update': 'inventory:slot_model_no_update',
        'cancel': 'inventory:slot_model_no_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(SlotModelNoDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


# --------------------------------------------
# Module Build Model Number CRUD
# --------------------------------------------
# Create your views here.
class ModuleBuildModelNoListView(ListView):
    model = ModuleBuildModelNo
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("module types", "/inventory/module_build_model_no_list/"),
        ("module type list", "/inventory/module_build_model_no_list")
    ]

    extra_context = {
        'breadcrumb_title': 'Module Build Model Number',
        'section_title': 'Module Build Model Number',
        'breadcrumb_path': path,
        'create': 'inventory:module_build_model_no_create',
        'delete': 'inventory:module_build_model_no_delete',
        'update': 'inventory:module_build_model_no_update',
        'cancel': 'inventory:module_build_model_no_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(ModuleBuildModelNoListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_queryset(self):
        queryset = ModuleBuildModelNo.objects.all()
        return queryset


class ModuleBuildModelNoUpdateView(UpdateView):
    model = ModuleBuildModelNo
    form_class = ModuleBuildModelNoForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("module build model numbers", '/inventory/module_build_model_no_list'),
        ("module build model number update", "/inventory/module_build_model_no_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Module Build Model Number Update',
        'section_title': 'Module Build Model Number Update',
        'breadcrumb_path': path,
        'create': 'inventory:module_build_model_no_create',
        'delete': 'inventory:module_build_model_no_delete',
        'update': 'inventory:module_build_model_no_update',
        'cancel': 'inventory:module_build_model_no_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(ModuleBuildModelNoUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class ModuleBuildModelNoCreateView(CreateView):
    model = ModuleBuildModelNo
    form_class = ModuleBuildModelNoForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("module build model numbers", '/inventory/module_build_model_no_list'),
        ("module build model number create", "/inventory/module_build_model_no_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Module Build Model Number Create',
        'section_title': 'Module Build Model Number Create',
        'breadcrumb_path': path,
        'create': 'inventory:module_build_model_no_create',
        'delete': 'inventory:module_build_model_no_delete',
        'update': 'inventory:module_build_model_no_update',
        'cancel': 'inventory:module_build_model_no_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(ModuleBuildModelNoCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class ModuleBuildModelNoDetailView(DetailView):
    model = ModuleBuildModelNo
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("module build model numbers", '/inventory/module_build_model_no_list'),
        ("module build model number detail", "/inventory/module_build_model_no_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Module Build Model Number Detail',
        'section_title': 'Module Build Model Number Detail',
        'breadcrumb_path': path,
        'create': 'inventory:module_build_model_no_create',
        'delete': 'inventory:module_build_model_no_delete',
        'update': 'inventory:module_build_model_no_update',
        'cancel': 'inventory:module_build_model_no_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(ModuleBuildModelNoDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class ModuleBuildModelNoDeleteView(DeleteView):
    model = ModuleBuildModelNo
    success_url = reverse_lazy('inventory:module_build_model_no_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("module build model numbers", 'inventory/module_build_model_no_list'),
        ("module build model number delete", "/inventory/module_build_model_no_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Module Build Model Number Delete',
        'section_title': 'Module Build Model Number Delete',
        'breadcrumb_path': path,
        'create': 'inventory:module_build_model_no_create',
        'delete': 'inventory:module_build_model_no_delete',
        'update': 'inventory:module_build_model_no_update',
        'cancel': 'inventory:module_build_model_no_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(ModuleBuildModelNoDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


# --------------------------------------------
# Chip Model Number CRUD
# --------------------------------------------
# Create your views here.
class ChipModelNoListView(ListView):
    model = ChipModelNo
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("chip model numbers", "/inventory/chip_model_no_list/"),
        ("chip model number list", "/inventory/chip_model_no_list")
    ]

    extra_context = {
        'breadcrumb_title': 'Chip Model Number',
        'section_title': 'Chip Model Numbers',
        'breadcrumb_path': path,
        'create': 'inventory:chip_model_no_create',
        'delete': 'inventory:chip_model_no_delete',
        'update': 'inventory:chip_model_no_update',
        'cancel': 'inventory:chip_model_no_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(ChipModelNoListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_queryset(self):
        queryset = ChipModelNo.objects.all()
        return queryset


class ChipModelNoUpdateView(UpdateView):
    model = ChipModelNo
    form_class = ChipModelNoForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("chip model numbers", '/inventory/chip_model_no_list'),
        ("chip model number update", "/inventory/chip_model_no_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Chip Model Number Update',
        'section_title': 'Chip Model Number Update',
        'breadcrumb_path': path,
        'create': 'inventory:chip_model_no_create',
        'delete': 'inventory:chip_model_no_delete',
        'update': 'inventory:chip_model_no_update',
        'cancel': 'inventory:chip_model_no_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(ChipModelNoUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class ChipModelNoCreateView(CreateView):
    model = ChipModelNo
    form_class = ChipModelNoForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("chip model numbers", '/inventory/chip_model_no_list'),
        ("chip model number create", "/inventory/chip_model_no_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Chip Model Number Create',
        'section_title': 'Chip Model Number Create',
        'breadcrumb_path': path,
        'create': 'inventory:chip_model_no_create',
        'delete': 'inventory:chip_model_no_delete',
        'update': 'inventory:chip_model_no_update',
        'cancel': 'inventory:chip_model_no_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(ChipModelNoCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class ChipModelNoDetailView(DetailView):
    model = ChipModelNo
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("chip model numbers", '/inventory/chip_model_no_list'),
        ("chip model number detail", "/inventory/chip_model_no_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Chip Model Number Detail',
        'section_title': 'Chip Model Number Detail',
        'breadcrumb_path': path,
        'create': 'inventory:chip_model_no_create',
        'delete': 'inventory:chip_model_no_delete',
        'update': 'inventory:chip_model_no_update',
        'cancel': 'inventory:chip_model_no_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(ChipModelNoDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class ChipModelNoDeleteView(DeleteView):
    model = ChipModelNo
    success_url = reverse_lazy('inventory:chip_model_no_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("chip model number", 'inventory/module_model_no_list'),
        ("chip model number delete", "/inventory/module_model_no_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Chip Model Number Delete',
        'section_title': 'Chip Model Number Delete',
        'breadcrumb_path': path,
        'create': 'inventory:chip_model_no_create',
        'delete': 'inventory:chip_model_no_delete',
        'update': 'inventory:chip_model_no_update',
        'cancel': 'inventory:chip_model_no_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(ChipModelNoDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context



























'''name = ''
serdes_num_front = ''
serdes_num_fabric = ''
serdes_speed_front = ''
serdes_speed_fabric = ''
model = ''
macs = []

chipset = {
    'name': name,
    'serdes_num_front': serdes_num_front,
    'serdes_num_fabric': serdes_num_fabric,
    'serdes_speed_front': serdes_speed_front,
    'serdes_speed_fabric': serdes_speed_fabric,
    'model': model,
}


name = ''
chipsets = []

module_build = {
    'name': name,
    'chipsets': chipsets,
}


name = ''
module_type = ''
ip = ''
module_build = ''
chassis = ''
slot = ''
serial = ''
state = ''


module = {
    'name': name,
    'module_type': module_type,
    'ip': ip,
    'module_build': module_build,
    'chassis': chassis,
    'slot': slot,
    'serial': serial,
    'state': state,
}

name = ''
description = ''
type = ''
slot = ''
number = ''
mac_addr = ''
ip = ''
speed = ''
state = ''
verified = ''
tx_bandwidth_utilization = ''
rx_bandwidth_utilization = ''


interface = {
    'name': name,
    'description': description,
    'type': type,
    'slot': slot,
    'number': number,
    'mac': mac_addr,
    'ip': ip,
    'speed': speed,
    'state': state,
    'verified': verified,
    'tx_bandwidth_utilization': tx_bandwidth_utilization,
    'rx_bandwidth_utilization': rx_bandwidth_utilization,
}

hostname = ''
fqdn = ''
serial = ''
model = ''
mac_addr = ''
num_slots = ''
state = ''
modules = []
interfaces = []

device = {
    'hostname': hostname,
    'fqdn': fqdn,
    'serial': serial,
    'mac': mac_addr,
    'num_slots': num_slots,
    'state': state,
    'model': model,
    'modules': modules,
    'interfaces': interfaces,
}'''


