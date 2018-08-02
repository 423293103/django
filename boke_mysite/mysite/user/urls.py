from django.urls import path
from . import views
urlpatterns=[
    path('no/', views.no, name='no'),
    path('', views.index, name='index'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login1, name='login'),
    path('register/', views.register, name='register'),
]
#path【准则，视图】捕获值,”准则“本质是一个参数