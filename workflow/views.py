from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, DeleteView
from .models import Step, StepType, StepState, StepAction, WorkflowType, WorkflowModel
from .forms import StepForm, StepTypeForm, StepStateForm, StepActionForm, WorkflowTypeForm, WorkflowModelForm
from django.urls import reverse_lazy


# --------------------------------------------
# Step CRUD
# --------------------------------------------
# Create your views here.
class StepListView(ListView):
    model = Step
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("workflows", "/workflow/workflow_type_list/"),
        ("step list", "/workflow/step_list")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step',
        'section_title': 'Steps',
        'breadcrumb_path': path,
        'create': 'workflow:step_create',
        'delete': 'workflow:step_delete',
        'update': 'workflow:step_update',
        'cancel': 'workflow:step_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(StepListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_queryset(self):
        queryset = Step.objects.all()
        return queryset


class StepUpdateView(UpdateView):
    model = Step
    form_class = StepForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("steps", '/workflow/step_list'),
        ("step update", "/workflow/step_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step Update',
        'section_title': 'Step Update',
        'breadcrumb_path': path,
        'create': 'workflow:step_create',
        'delete': 'workflow:step_delete',
        'update': 'workflow:step_update',
        'cancel': 'workflow:step_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(StepUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class StepCreateView(CreateView):
    model = Step
    form_class = StepForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("steps", '/workflow/step_list'),
        ("step create", "/workflow/step_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step Create',
        'section_title': 'Step Create',
        'breadcrumb_path': path,
        'create': 'workflow:step_create',
        'delete': 'workflow:step_delete',
        'update': 'workflow:step_update',
        'cancel': 'workflow:step_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(StepCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class StepDetailView(DetailView):
    model = Step
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("steps", '/workflow/step_list'),
        ("step detail", "/workflow/step_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step Detail',
        'section_title': 'Step Detail',
        'breadcrumb_path': path,
        'create': 'workflow:step_create',
        'delete': 'workflow:step_delete',
        'update': 'workflow:step_update',
        'cancel': 'workflow:step_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(StepDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    '''def get_queryset(self):
        queryset = Step.objects.get(pk=self.kwargs['pk'])
        return queryset'''


class StepDeleteView(DeleteView):
    model = Step
    success_url = reverse_lazy('workflow:step_type_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("steps", '/workflow/step_list'),
        ("step delete", "/workflow/step_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step Delete',
        'section_title': 'Step Delete',
        'breadcrumb_path': path,
        'create': 'workflow:step_create',
        'delete': 'workflow:step_delete',
        'update': 'workflow:step_update',
        'cancel': 'workflow:step_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(StepDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


# --------------------------------------------
# Step Type CRUD
# --------------------------------------------
class StepTypeListView(ListView):
    model = StepType
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("workflows", "/workflow/workflow_type_list/"),
        ("step type list", "/workflow/step_type_list")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step Type',
        'section_title': 'Step Types',
        'breadcrumb_path': path,
        'create': 'workflow:step_type_create',
        'delete': 'workflow:step_type_delete',
        'update': 'workflow:step_type_update',
        'cancel': 'workflow:step_type_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(StepTypeListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class StepTypeUpdateView(UpdateView):
    model = StepType
    form_class = StepTypeForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("step types", '/workflow/step_type_list'),
        ("step type update", "/workflow/step_type_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step Type Update',
        'section_title': 'Step Type Update',
        'breadcrumb_path': path,
        'create': 'workflow:step_type_create',
        'delete': 'workflow:step_type_delete',
        'update': 'workflow:step_type_update',
        'cancel': 'workflow:step_type_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(StepTypeUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class StepTypeCreateView(CreateView):
    model = StepType
    form_class = StepTypeForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("step types", '/workflow/step_type_list'),
        ("step type create", "/workflow/step_type_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step Type Create',
        'section_title': 'Step Type Create',
        'breadcrumb_path': path,
        'create': 'workflow:step_type_create',
        'delete': 'workflow:step_type_delete',
        'update': 'workflow:step_type_update',
        'cancel': 'workflow:step_type_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(StepTypeCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class StepTypeDetailView(DetailView):
    model = StepType
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("step types", '/workflow/step_type_list'),
        ("step type detail", "/workflow/step_type_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step Type Detail',
        'section_title': 'Step Type Detail',
        'breadcrumb_path': path,
        'create': 'workflow:step_type_create',
        'delete': 'workflow:step_type_delete',
        'update': 'workflow:step_type_update',
        'cancel': 'workflow:step_type_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(StepTypeDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class StepTypeDeleteView(DeleteView):
    model = StepType
    success_url = reverse_lazy('workflow:step_type_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("step types", '/workflow/step_type_list'),
        ("step type delete", "/workflow/step_type_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step Type Delete',
        'section_title': 'Step Type Delete',
        'breadcrumb_path': path,
        'create': 'workflow:step_type_create',
        'delete': 'workflow:step_type_delete',
        'update': 'workflow:step_type_update',
        'cancel': 'workflow:step_type_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(StepTypeDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


# --------------------------------------------
# Step State CRUD
# --------------------------------------------
class StepStateListView(ListView):
    model = StepState
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("workflows", "/workflow/workflow_type_list/"),
        ("step state list", "/workflow/step_state_list")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step State',
        'section_title': 'Step State',
        'breadcrumb_path': path,
        'create': 'workflow:step_state_create',
        'delete': 'workflow:step_state_delete',
        'update': 'workflow:step_state_update',
        'cancel': 'workflow:step_state_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(StepStateListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class StepStateUpdateView(UpdateView):
    model = StepState
    form_class = StepStateForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("step states", '/workflow/step_state_list'),
        ("step state update", "/workflow/step_state_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step State Update',
        'section_title': 'Step State Update',
        'breadcrumb_path': path,
        'create': 'workflow:step_state_create',
        'delete': 'workflow:step_state_delete',
        'update': 'workflow:step_state_update',
        'cancel': 'workflow:step_state_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(StepStateUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class StepStateCreateView(CreateView):
    model = StepState
    form_class = StepStateForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("step states", '/workflow/step_state_list'),
        ("step state create", "/workflow/step_state_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step State Create',
        'section_title': 'Step State Create',
        'breadcrumb_path': path,
        'create': 'workflow:step_state_create',
        'delete': 'workflow:step_state_delete',
        'update': 'workflow:step_state_update',
        'cancel': 'workflow:step_state_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(StepStateCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class StepStateDetailView(DetailView):
    model = StepState
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("step states", '/workflow/step_state_list'),
        ("step state detail", "/workflow/step_state_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step State Detail',
        'section_title': 'Step State Detail',
        'breadcrumb_path': path,
        'create': 'workflow:step_state_create',
        'delete': 'workflow:step_state_delete',
        'update': 'workflow:step_state_update',
        'cancel': 'workflow:step_state_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(StepStateDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class StepStateDeleteView(DeleteView):
    model = StepState
    success_url = reverse_lazy('workflow:step_state_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("step states", '/workflow/step_type_list'),
        ("step state delete", "/workflow/step_state_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step State Delete',
        'section_title': 'Step State Delete',
        'breadcrumb_path': path,
        'create': 'workflow:step_state_create',
        'delete': 'workflow:step_state_delete',
        'update': 'workflow:step_state_update',
        'cancel': 'workflow:step_state_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(StepStateDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


# --------------------------------------------
# Step Action CRUD
# --------------------------------------------
class StepActionListView(ListView):
    model = StepAction
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("workflows", "/workflow/workflow_type_list/"),
        ("step action list", "/workflow/step_action_list")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step Action',
        'section_title': 'Step Action',
        'breadcrumb_path': path,
        'create': 'workflow:step_action_create',
        'delete': 'workflow:step_action_delete',
        'update': 'workflow:step_action_update',
        'cancel': 'workflow:step_action_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(StepActionListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class StepActionUpdateView(UpdateView):
    model = StepAction
    form_class = StepActionForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("step actions", '/workflow/step_action_list'),
        ("step action update", "/workflow/step_action_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step Action Update',
        'section_title': 'Step Action Update',
        'breadcrumb_path': path,
        'create': 'workflow:step_action_create',
        'delete': 'workflow:step_action_delete',
        'update': 'workflow:step_action_update',
        'cancel': 'workflow:step_action_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(StepActionUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class StepActionCreateView(CreateView):
    model = StepAction
    form_class = StepActionForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("step actions", '/workflow/step_action_list'),
        ("step action create", "/workflow/step_action_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step Action Create',
        'section_title': 'Step Action Create',
        'breadcrumb_path': path,
        'create': 'workflow:step_action_create',
        'delete': 'workflow:step_action_delete',
        'update': 'workflow:step_action_update',
        'cancel': 'workflow:step_action_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(StepActionCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class StepActionDetailView(DetailView):
    model = StepAction
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("step actions", '/workflow/step_action_list'),
        ("step action detail", "/workflow/step_action_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step Action Detail',
        'section_title': 'Step Action Detail',
        'breadcrumb_path': path,
        'create': 'workflow:step_action_create',
        'delete': 'workflow:step_action_delete',
        'update': 'workflow:step_action_update',
        'cancel': 'workflow:step_action_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(StepActionDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class StepActionDeleteView(DeleteView):
    model = StepAction
    success_url = reverse_lazy('workflow:step_action_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("step actions", '/workflow/step_action_list'),
        ("step action delete", "/workflow/step_action_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Step Action Delete',
        'section_title': 'Step Action Delete',
        'breadcrumb_path': path,
        'create': 'workflow:step_action_create',
        'delete': 'workflow:step_action_delete',
        'update': 'workflow:step_action_update',
        'cancel': 'workflow:step_action_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(StepActionDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


# --------------------------------------------
# Workflow Type CRUD
# --------------------------------------------
class WorkflowTypeListView(ListView):
    model = WorkflowType
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("workflow types", "/workflow/workflow_type_list/"),
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Type',
        'section_title': 'Workflow Type',
        'breadcrumb_path': path,
        'create': 'workflow:workflow_type_create',
        'delete': 'workflow:workflow_type_delete',
        'update': 'workflow:workflow_type_update',
        'cancel': 'workflow:workflow_type_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(WorkflowTypeListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class WorkflowTypeUpdateView(UpdateView):
    model = WorkflowType
    form_class = WorkflowTypeForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("workflow types", '/workflow/workflow_type_list'),
        ("workflow type update", "/workflow/workflow_type_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Type Update',
        'section_title': 'Workflow Type Update',
        'breadcrumb_path': path,
        'create': 'workflow:workflow_type_create',
        'delete': 'workflow:workflow_type_delete',
        'update': 'workflow:workflow_type_update',
        'cancel': 'workflow:workflow_type_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(WorkflowTypeUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class WorkflowTypeCreateView(CreateView):
    model = WorkflowType
    form_class = WorkflowTypeForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("workflow types", '/workflow/workflow_type_list'),
        ("workflow type create", "/workflow/workflow_type_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Type Create',
        'section_title': 'Workflow Type Create',
        'breadcrumb_path': path,
        'create': 'workflow:workflow_type_create',
        'delete': 'workflow:workflow_type_delete',
        'update': 'workflow:workflow_type_update',
        'cancel': 'workflow:workflow_type_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(WorkflowTypeCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class WorkflowTypeDetailView(DetailView):
    model = WorkflowType
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("workflow types", '/workflow/workflow_type_list'),
        ("workflow type detail", "/workflow/workflow_type_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Type Detail',
        'section_title': 'Workflow Type Detail',
        'breadcrumb_path': path,
        'create': 'workflow:workflow_type_create',
        'delete': 'workflow:workflow_type_delete',
        'update': 'workflow:workflow_type_update',
        'cancel': 'workflow:workflow_type_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(WorkflowTypeDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class WorkflowTypeDeleteView(DeleteView):
    model = WorkflowType
    success_url = reverse_lazy('workflow:workflow_type_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("workflow types", '/workflow/workflow_type_list'),
        ("workflow type delete", "/workflow/workflow_type_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Type Delete',
        'section_title': 'Workflow Type Delete',
        'breadcrumb_path': path,
        'create': 'workflow:workflow_type_create',
        'delete': 'workflow:workflow_type_delete',
        'update': 'workflow:workflow_type_update',
        'cancel': 'workflow:workflow_type_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(WorkflowTypeDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


# --------------------------------------------
# Workflow Model CRUD
# --------------------------------------------
class WorkflowModelListView(ListView):
    model = WorkflowModel
    template_name = 'workflow/list.html'

    path = [
        ("home", "account:index"),
        ("workflow models", "/workflow/workflow_model_list/"),
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Model',
        'section_title': 'Workflow Model',
        'breadcrumb_path': path,
        'create': 'workflow:workflow_model_create',
        'delete': 'workflow:workflow_model_delete',
        'update': 'workflow:workflow_model_update',
        'cancel': 'workflow:workflow_model_list',
        'icon': 'mdi-format-list-bulleted',
    }

    def get_context_data(self, **kwargs):
        context = super(WorkflowModelListView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class WorkflowModelUpdateView(UpdateView):
    model = WorkflowModel
    form_class = WorkflowModelForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("workflow models", '/workflow/workflow_model_list'),
        ("workflow model update", "/workflow/workflow_model_update")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Model Update',
        'section_title': 'Workflow Model Update',
        'breadcrumb_path': path,
        'create': 'workflow:workflow_model_create',
        'delete': 'workflow:workflow_model_delete',
        'update': 'workflow:workflow_model_update',
        'cancel': 'workflow:workflow_model_list',
        'icon': 'fa fa-edit',
    }

    def get_context_data(self, **kwargs):
        context = super(WorkflowModelUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class WorkflowModelCreateView(CreateView):
    model = WorkflowModel
    form_class = WorkflowModelForm
    template_name = 'workflow/form.html'

    path = [
        ("home", "account:index"),
        ("workflow models", '/workflow/workflow_model_list'),
        ("workflow model create", "/workflow/workflow_model_create")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Model Create',
        'section_title': 'Workflow Model Create',
        'breadcrumb_path': path,
        'create': 'workflow:workflow_model_create',
        'delete': 'workflow:workflow_model_delete',
        'update': 'workflow:workflow_model_update',
        'cancel': 'workflow:workflow_model_list',
        'icon': 'fa fa-plus',
    }

    def get_context_data(self, **kwargs):
        context = super(WorkflowModelCreateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class WorkflowModelDetailView(DetailView):
    model = WorkflowModel
    template_name = 'workflow/detail.html'

    path = [
        ("home", "account:index"),
        ("workflow models", '/workflow/workflow_model_list'),
        ("workflow model detail", "/workflow/workflow_model_view")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Model Detail',
        'section_title': 'Workflow Model Detail',
        'breadcrumb_path': path,
        'create': 'workflow:workflow_model_create',
        'delete': 'workflow:workflow_model_delete',
        'update': 'workflow:workflow_model_update',
        'cancel': 'workflow:workflow_model_list',
        'icon': 'fa fa-cogs',
    }

    def get_context_data(self, **kwargs):
        context = super(WorkflowModelDetailView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class WorkflowModelDeleteView(DeleteView):
    model = WorkflowModel
    success_url = reverse_lazy('workflow:workflow_model_list')
    template_name = 'workflow/confirm_delete.html'

    path = [
        ("home", "account:index"),
        ("workflow models", '/workflow/workflow_model_list'),
        ("workflow model delete", "/workflow/workflow_model_delete")
    ]

    extra_context = {
        'breadcrumb_title': 'Workflow Model Delete',
        'section_title': 'Workflow Model Delete',
        'breadcrumb_path': path,
        'create': 'workflow:workflow_model_create',
        'delete': 'workflow:workflow_model_delete',
        'update': 'workflow:workflow_model_update',
        'cancel': 'workflow:workflow_model_list',
        'icon': 'mdi-delete-variant',
    }

    def get_context_data(self, **kwargs):
        context = super(WorkflowModelDeleteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
