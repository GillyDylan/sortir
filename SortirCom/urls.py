from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from SortirCom import views

urlpatterns = [
    path('coco<varTest>', views.workspace)
]