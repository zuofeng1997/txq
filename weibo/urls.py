from django.urls import path
from . import views
app_name = 'weibo'
urlpatterns = [
    path('showuser/<int:id>',views.showuser,name='showuser'),
    path("showweibo/<int:id>/<int:weiboid>",views.showweibo,name="showweibo"),
    path("showotheruser/<int:id>",views.showotheruser,name="showotheruser"),

]