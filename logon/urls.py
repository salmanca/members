from django.urls import path
from . import views

urlpatterns = [
    # path('', views.baseView, name="base" ),
    path('', views.login_user, name="login" ),
    path('home', views.baseView, name= "home"),
    path('login',views.logout_user, name="logout"),
]
