from django.urls import path
from . import views

urlpatterns = [
    
    path('novaadmin',views.novaadmin,name="novaadmin"),
    path('emplogin',views.emplogin,name="emplogin"),
    path('dipierieo',views.dipierieo,name="dipierieo"),
    path('guevara',views.guevara,name="auevara"),
    #path('allusrs',views.allusrs,name="allusrs"),
    path('dataall',views.dataall,name="dataall"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('empdashboard',views.empdashboard,name="empdashboard"),
    path('manage',views.manage,name="manage"),
    path('manageclients',views.manageclients,name="manageclients"),
    path('addclients',views.addclients,name="addclients"), 
    path('supportlist',views.supportlist,name="supportlist"),
    path('autofresh',views.autofresh,name="autofresh"),
    path('empmanage',views.empmanage,name='empmanage'),
    path('cred',views.cred,name='cred'),
    path('suportmng',views.suportmng,name='suportmng'),
    path('empchk',views.empchk,name='empchk'),
    path('timesheet',views.timesheet,name='timesheet'),
    path('emptimesheet',views.emptimesheet,name='emptimesheet'),
    path('exporttime',views.exporttime,name='exporttime'),
    
    
    
]