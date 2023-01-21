from django.urls import path 
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('loginuser',views.login_user,name='loginuser'),
    path('logout',views.logout_view,name='logout'),
    path('otp',views.verifyotp,name='otp'),
]
