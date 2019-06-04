from django.conf.urls import url
from . import views

app_name = 'workflow'

urlpatterns = [
    # /workflow/
    url(r'^step_list/$', views.StepListView.as_view(), name='step_list'),
    url(r'^step_create/$', views.StepCreateView.as_view(), name='step_create'),
    url(r'^step_update/(?P<pk>\d+)$', views.StepUpdateView.as_view(), name='step_update'),
    url(r'^step_view/(?P<pk>\d+)$', views.StepDetailView.as_view(), name='step_view'),
    url(r'^step_delete/(?P<pk>\d+)$', views.StepDeleteView.as_view(), name='step_delete'),

    url(r'^step_type_list/$', views.StepTypeListView.as_view(), name='step_type_list'),
    url(r'^step_type_create/$', views.StepTypeCreateView.as_view(), name='step_type_create'),
    url(r'^step_type_update/(?P<pk>\d+)$', views.StepTypeUpdateView.as_view(), name='step_type_update'),
    url(r'^step_type_view/(?P<pk>\d+)$', views.StepTypeDetailView.as_view(), name='step_type_view'),
    url(r'^step_type_delete/(?P<pk>\d+)$', views.StepTypeDeleteView.as_view(), name='step_type_delete'),

    url(r'^step_state_list/$', views.StepStateListView.as_view(), name='step_state_list'),
    url(r'^step_state_create/$', views.StepStateCreateView.as_view(), name='step_state_create'),
    url(r'^step_state_update/(?P<pk>\d+)$', views.StepStateUpdateView.as_view(), name='step_state_update'),
    url(r'^step_state_view/(?P<pk>\d+)$', views.StepStateDetailView.as_view(), name='step_state_view'),
    url(r'^step_state_delete/(?P<pk>\d+)$', views.StepStateDeleteView.as_view(), name='step_state_delete'),

    url(r'^step_action_list/$', views.StepActionListView.as_view(), name='step_action_list'),
    url(r'^step_action_create/$', views.StepActionCreateView.as_view(), name='step_action_create'),
    url(r'^step_action_update/(?P<pk>\d+)$', views.StepActionUpdateView.as_view(), name='step_action_update'),
    url(r'^step_action_view/(?P<pk>\d+)$', views.StepActionDetailView.as_view(), name='step_action_view'),
    url(r'^step_action_delete/(?P<pk>\d+)$', views.StepActionDeleteView.as_view(), name='step_action_delete'),

    url(r'^workflow_type_list/$', views.WorkflowTypeListView.as_view(), name='workflow_type_list'),
    url(r'^workflow_type_create/$', views.WorkflowTypeCreateView.as_view(), name='workflow_type_create'),
    url(r'^workflow_type_update/(?P<pk>\d+)$', views.WorkflowTypeUpdateView.as_view(), name='workflow_type_update'),
    url(r'^workflow_type_view/(?P<pk>\d+)$', views.WorkflowTypeDetailView.as_view(), name='workflow_type_view'),
    url(r'^workflow_type_delete/(?P<pk>\d+)$', views.WorkflowTypeDeleteView.as_view(), name='workflow_type_delete'),

    url(r'^workflow_model_list/$', views.WorkflowModelListView.as_view(), name='workflow_model_list'),
    url(r'^workflow_model_create/$', views.WorkflowModelCreateView.as_view(), name='workflow_model_create'),
    url(r'^workflow_model_update/(?P<pk>\d+)$', views.WorkflowModelUpdateView.as_view(), name='workflow_model_update'),
    url(r'^workflow_model_view/(?P<pk>\d+)$', views.WorkflowModelDetailView.as_view(), name='workflow_model_view'),
    url(r'^workflow_model_delete/(?P<pk>\d+)$', views.WorkflowModelDeleteView.as_view(), name='workflow_model_delete'),
]

