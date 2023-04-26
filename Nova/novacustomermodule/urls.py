from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('support',views.support,name="support"),
    path('customer',views.customer,name="customer"),
    path('uploads',views.uploads,name="uploads"),
    path('any',views.any,name="any"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('sprtupdate',views.sprtupdate,name="sprtupdate")
    
   
   ]