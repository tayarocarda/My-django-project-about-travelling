from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageListView.as_view(), name='page_list'),
    path('page/<slug:slug>/', views.PageDetailView.as_view(), name='page_detail'),
]