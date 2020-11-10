from django.urls import path
from authentication.views import login, register,logout,RegisterAPI,LoginAPI



urlpatterns = [
    path('login/', login,name="logout"),
    path('register/', register,name='register'),
    path('logout/',logout,name="logout"),

    #login ,register api route 
    path('api/register/', RegisterAPI.as_view(), name='api_register'),
    path('api/login/', LoginAPI.as_view(), name='api_login'),
]
