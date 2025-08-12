from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('add/', views.expense_add, name='expense_add'),
    path('edit/<int:pk>/', views.expense_edit, name='expense_edit'),
    path('delete/<int:pk>/', views.expense_delete, name='expense_delete'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
    path('analytics/', views.analytics, name='analytics'),
    path('budget/', views.manage_budget, name='manage_budget'),
]
