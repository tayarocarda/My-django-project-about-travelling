from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_list, name='page_list'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('<slug:slug>/', views.page_detail, name='page_detail'),
]