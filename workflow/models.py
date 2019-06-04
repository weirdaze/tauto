from django.db import models
from django.shortcuts import reverse

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


# Create your models here.
class StepType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workflow:step_type_view', args=[str(self.pk)])


class StepState(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workflow:step_state_view', args=[str(self.pk)])


class StepAction(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workflow:step_action_view', args=[str(self.pk)])


class Step(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    type = models.ForeignKey(StepType, on_delete=models.CASCADE)
    action = models.ForeignKey(StepAction, on_delete=models.DO_NOTHING)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workflow:step_view', args=[str(self.pk)])


class WorkflowType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workflow:workflow_type_view', args=[str(self.pk)])


class WorkflowModel(models.Model):
    name = models.CharField(max_length=200)
    step = GenericRelation(Step)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workflow:workflow_model_view', args=[str(self.pk)])


class StepInstance(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    state = models.ForeignKey(StepState, on_delete=models.DO_NOTHING)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.step.name


class WorkflowInstance(models.Model):
    workflow = models.ForeignKey(WorkflowModel, on_delete=models.CASCADE)
    step = GenericRelation(StepInstance)

    def __str__(self):
        return self.workflow.name
