from django.conf.urls import url
from . import views

app_name = 'device_model'

urlpatterns = [
    # /inventory/
    url(r'^device_type_list/$', views.DeviceTypeListView.as_view(), name='device_type_list'),
    url(r'^device_type_create/$', views.DeviceTypeCreateView.as_view(), name='device_type_create'),
    url(r'^device_type_update/(?P<pk>\d+)$', views.DeviceTypeUpdateView.as_view(), name='device_type_update'),
    url(r'^device_type_view/(?P<pk>\d+)$', views.DeviceTypeDetailView.as_view(), name='device_type_view'),
    url(r'^device_type_delete/(?P<pk>\d+)$', views.DeviceTypeDeleteView.as_view(), name='device_type_delete'),

    url(r'^serdes_type_list/$', views.SerdesTypeListView.as_view(), name='serdes_type_list'),
    url(r'^serdes_type_create/$', views.SerdesTypeCreateView.as_view(), name='serdes_type_create'),
    url(r'^serdes_type_update/(?P<pk>\d+)$', views.SerdesTypeUpdateView.as_view(), name='serdes_type_update'),
    url(r'^serdes_type_view/(?P<pk>\d+)$', views.SerdesTypeDetailView.as_view(), name='serdes_type_view'),
    url(r'^serdes_type_delete/(?P<pk>\d+)$', views.SerdesTypeDeleteView.as_view(), name='serdes_type_delete'),

    url(r'^slot_type_list/$', views.SlotTypeListView.as_view(), name='slot_type_list'),
    url(r'^slot_type_create/$', views.SlotTypeCreateView.as_view(), name='slot_type_create'),
    url(r'^slot_type_update/(?P<pk>\d+)$', views.SlotTypeUpdateView.as_view(), name='slot_type_update'),
    url(r'^slot_type_view/(?P<pk>\d+)$', views.SlotTypeDetailView.as_view(), name='slot_type_view'),
    url(r'^slot_type_delete/(?P<pk>\d+)$', views.SlotTypeDeleteView.as_view(), name='slot_type_delete'),

    url(r'^module_type_list/$', views.ModuleTypeListView.as_view(), name='module_type_list'),
    url(r'^module_type_create/$', views.ModuleTypeCreateView.as_view(), name='module_type_create'),
    url(r'^module_type_update/(?P<pk>\d+)$', views.ModuleTypeUpdateView.as_view(), name='module_type_update'),
    url(r'^module_type_view/(?P<pk>\d+)$', views.ModuleTypeDetailView.as_view(), name='module_type_view'),
    url(r'^module_type_delete/(?P<pk>\d+)$', views.ModuleTypeDeleteView.as_view(), name='module_type_delete'),

    url(r'^chip_type_list/$', views.ChipTypeListView.as_view(), name='chip_type_list'),
    url(r'^chip_type_create/$', views.ChipTypeCreateView.as_view(), name='chip_type_create'),
    url(r'^chip_type_update/(?P<pk>\d+)$', views.ChipTypeUpdateView.as_view(), name='chip_type_update'),
    url(r'^chip_type_view/(?P<pk>\d+)$', views.ChipTypeDetailView.as_view(), name='chip_type_view'),
    url(r'^chip_type_delete/(?P<pk>\d+)$', views.ChipTypeDeleteView.as_view(), name='chip_type_delete'),

    # ---- Model Numbers
    url(r'^device_model_no_list/$', views.DeviceModelNoListView.as_view(), name='device_model_no_list'),
    url(r'^device_model_no_create/$', views.DeviceModelNoCreateView.as_view(), name='device_model_no_create'),
    url(r'^device_model_no_update/(?P<pk>\d+)$', views.DeviceModelNoUpdateView.as_view(), name='device_model_no_update'),
    url(r'^device_model_no_view/(?P<pk>\d+)$', views.DeviceModelNoDetailView.as_view(), name='device_model_no_view'),
    url(r'^device_model_no_delete/(?P<pk>\d+)$', views.DeviceModelNoDeleteView.as_view(), name='device_model_no_delete'),

    url(r'^slot_model_no_list/$', views.SlotModelNoListView.as_view(), name='slot_model_no_list'),
    url(r'^slot_model_no_create/$', views.SlotModelNoCreateView.as_view(), name='slot_model_no_create'),
    url(r'^slot_model_no_update/(?P<pk>\d+)$', views.SlotModelNoUpdateView.as_view(), name='slot_model_no_update'),
    url(r'^slot_model_no_view/(?P<pk>\d+)$', views.SlotModelNoDetailView.as_view(), name='slot_model_no_view'),
    url(r'^slot_model_no_delete/(?P<pk>\d+)$', views.SlotModelNoDeleteView.as_view(), name='slot_model_no_delete'),

    url(r'^module_build_model_no_list/$', views.ModuleBuildModelNoListView.as_view(), name='module_build_model_no_list'),
    url(r'^module_build_model_no_create/$', views.ModuleBuildModelNoCreateView.as_view(), name='module_build_model_no_create'),
    url(r'^module_build_model_no_update/(?P<pk>\d+)$', views.ModuleBuildModelNoUpdateView.as_view(), name='module_build_model_no_update'),
    url(r'^module_build_model_no_view/(?P<pk>\d+)$', views.ModuleBuildModelNoDetailView.as_view(), name='module_build_model_no_view'),
    url(r'^module_build_model_no_delete/(?P<pk>\d+)$', views.ModuleBuildModelNoDeleteView.as_view(), name='module_build_model_no_delete'),

    url(r'^chip_model_no_list/$', views.ChipModelNoListView.as_view(), name='chip_model_no_list'),
    url(r'^chip_model_no_create/$', views.ChipModelNoCreateView.as_view(), name='chip_model_no_create'),
    url(r'^chip_model_no_update/(?P<pk>\d+)$', views.ChipModelNoUpdateView.as_view(), name='chip_model_no_update'),
    url(r'^chip_model_no_view/(?P<pk>\d+)$', views.ChipModelNoDetailView.as_view(), name='chip_model_no_view'),
    url(r'^chip_model_no_delete/(?P<pk>\d+)$', views.ChipModelNoDeleteView.as_view(), name='chip_model_no_delete'),
]
