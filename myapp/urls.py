from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('regions/', views.regions, name='regions'),
    path('attractions/', views.attractions, name='attractions'),
    path('routes/', views.routes, name='routes'),
    path('tips/', views.tips, name='tips'),
    path('task1/', views.task1, name='task1'),
    path('task2/', views.task2, name='task2'),
    path('design-school/', views.design_school, name='design_school'),
]