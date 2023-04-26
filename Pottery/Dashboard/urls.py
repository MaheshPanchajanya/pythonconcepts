from django.urls import path
from . import views

urlpatterns = [

    path("dboardlogin",views.dboardlogin,name="dboardlogin"),
    path("dlogout",views.dlogout,name="dlogout"),
    path("dasboard",views.dasboard,name="dasboard"),
    path("removeorder",views.removeorder,name="removeorder")
]