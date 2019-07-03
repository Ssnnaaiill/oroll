from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'oroll'

urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name = 'index'),
        url(r'^upload$', views.upload, name = 'upload')
]
