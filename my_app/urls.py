"""my_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from home.views import home_view
from faq.views import faq_view
from data.views import res_view,index_view
from discuss.views import discussion
from survey.views import survey_view,thanks_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='index'),
    path('res', res_view, name='res'),
    path('faq', faq_view, name='faq'),
    path('', index_view, name='index'),
    path('discuss',discussion, name='discuss'),
    path('survey',survey_view, name='survey'),
    path('thanks',thanks_view, name='thanks'),
]
