"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import include, path
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib import admin
from django.urls import path


admin.site.site_header = "My Administration"
admin.site.site_title = "My Admin"
admin.site.enable_nav_sidebar = False


def home(request):
    #host = request.headers.get("host")
    return redirect(reverse("kmuhelper:home"))


urlpatterns = [
    path('kmuhelper/', include('kmuhelper.urls')),
    path('admin/', admin.site.urls),
    path('', home),
    path(
        'pwreset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset',
    ),
    path(
        'pwreset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'pwreset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'pwreset/complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
]


if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
