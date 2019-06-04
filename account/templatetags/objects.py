from django import template
from workflow.models import StepAction

register = template.Library()


@register.filter(name='get_fields')
def get_fields(object_id):
    return object_id._meta.fields


@register.filter(name='parse_field_name')
def parse_field_name(field):
    return field.name


@register.filter(name='parse_object_type')
def parse_object_type(field):
    print(type(field).get_attname)
    return ''


@register.filter(name='parse_field_value')
def parse_field_value(object, field):
    field_name = field.name
    my_model = type(object)
    obj = my_model.objects.get(name=str(object))
    field_object = my_model._meta.get_field(field_name)
    field_value = field_object.value_from_object(obj)

    '''print("object: " + str(object))
    print("field: " + str(field))
    print("field_name: " + str(field_name))
    print("my_model: " + str(my_model))
    print("obj: " + str(obj))
    print("field_object: " + str(field_object))
    print("field_value: " + str(field_value))'''

    return field_value


@register.filter(name='parse_action_object')
def parse_action_object(field_value):
    action = StepAction.objects.get(pk=field_value)
    return action
