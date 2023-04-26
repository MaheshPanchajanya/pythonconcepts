from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('view_category',views.view_category,name="view_category"),
    path('special',views.special,name="special"),
    path('contact_dealer',views.contact_dealer,name="contact_dealer"),
    path('about_potterycrafts',views.about_potterycrafts,name="about_potterycrafts"),
    path('pottery_blogs',views.potteryfeeds,name='pottery_blogs'),
    path('removeordr',views.removeordr,name='removeordr'),
    path('special2',views.special2,name='special2'),
    path('quotechk',views.quotechk,name='quotechk'),
]

