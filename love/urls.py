from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accept',views.accept,name='accept'),
    path('reject',views.reject,name='reject')
]