from django.urls import path
from .import views

urlpatterns = [

    path('',views.app),
    path('home/',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('index/add',views.addbus,name='addbus'),
    path('home/table/',views.table,name='view'),
    path('update/(?P<pk>\w+)',views.update,name="update"),
    path('delete/(?P<pk>\w+)',views.delete,name="delete"),
	path('accounts/login/',views.loginview,name="login"),
	path('home/logout',views.logout_view),
	path('accounts/sign_up/',views.sign_up,name="signup") ,
	path('reset',views.Resethome,name='reset'), 
	path('passwordreset',views.resetPassword,name="passwordreset"),
    
    path('index2/',views.index2),
    
]