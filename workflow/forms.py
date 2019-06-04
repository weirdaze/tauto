from django import forms
from .models import Step, StepType, StepState, StepAction, WorkflowModel, WorkflowType


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['name', 'description', 'active', 'order', 'type', 'action']


class StepTypeForm(forms.ModelForm):
    class Meta:
        model = StepType
        fields = ['name']


class StepStateForm(forms.ModelForm):
    class Meta:
        model = StepState
        fields = ['name']


class StepActionForm(forms.ModelForm):
    class Meta:
        model = StepAction
        fields = ['name']


class WorkflowTypeForm(forms.ModelForm):
    class Meta:
        model = WorkflowType
        fields = ['name']


class WorkflowModelForm(forms.ModelForm):
    class Meta:
        model = WorkflowModel
        fields = ['name']