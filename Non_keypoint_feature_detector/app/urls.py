from django.urls import path,include
from app.views import *

urlpatterns = [
    path("",home,name="home"),
    path("filter/<int:num>",filter_view,name = "filter"),
]
