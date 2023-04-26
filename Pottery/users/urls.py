from django.urls import path
from . import views

urlpatterns=[
    path('login',views.login,name="login"),
  #  path('register',views.registration,name="register"),
    path('logout',views.logout,name="logout"),
   # path('sendmsg',views.sendmsg,name='sendmsg')
 #   path('<int:ld>/',views.useraccount,name="useraccount")
]