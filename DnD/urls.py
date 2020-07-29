"""DnD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import os
from django.views.static import serve
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from app.views import SubmitFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submitForm/',SubmitFormView.as_view()),
    url(r'^fp/', include('django_drf_filepond.urls')),
    url(r'^demo/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.BASE_DIR,'templates')}),

]
