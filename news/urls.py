from django.conf.urls import url
from django.urls import path
from news import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:pk>', views.news_detail, name='news_detail'),
]
