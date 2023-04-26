from django.urls import path
from .  import views

urlpatterns=[
    path('loadpatch',views.loadpatch,name="loadpatch")]