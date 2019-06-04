"""tauto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account.regbackend import MyRegistrationView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('account.urls')),
    url(r'^workflow/', include('workflow.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(), name='auth_login'),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='auth_logout'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # /password-reset/
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        from_email='elliott.castillo@sitenaut.com',
        html_email_template_name='registration/password_reset_html_email.html',
        subject_template_name='registration/password_reset_subject.txt'
    ), name='password_reset'),

    # /password-reset/done
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),

    # /password-reset/confirm
    path('password-reset/confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)