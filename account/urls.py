from django.urls import path
from . import views

urlpatterns = [
    path('login',views.signin,name="signin"),
    path('register',views.register,name="register"),
    path('register-user',views.reguser,name="reguser"),
    path('login-user',views.loginuser,name="loginuser"),
    path('logout',views.log_out,name="logout"),
]
