from django.urls import path
from .import views

urlpatterns = [
  
    path('',views.table,name='table'),
    path('search/',views.bus_search,name='bus_search'),
    path('index1/',views.index1),

]