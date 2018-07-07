from django.urls import path
from . import views
app_name = 'login'
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login, name='login'),
    path('success/',views.success,name='success'),
    path('register/',views.register,name='register')
]