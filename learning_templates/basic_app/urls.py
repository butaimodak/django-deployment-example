from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    # Other urlpatterns
    
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]

