from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),

    path("categories/", views.CategoryListView.as_view(), name='category_list'),
    path('new_category/', views.CategoryCreateView.as_view(), name='new_category'),
    path("category/<int:pk>/", views.CategoryDetailView.as_view(), name='category_detail'),
    path("category/<int:pk>/edit", views.CategoryUpdateView.as_view(), name='category_edit'),
    path("category/<int:pk>/delete", views.CategoryDeleteView.as_view(), name='category_delete'),

    path('list_receivables/', views.list_receivables, name='list_receivables'),

    path('list_items/', views.list_item, name='list_items'),
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    path('add_items/', views.add_items, name='add_items'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
    path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),
    path('list_history/', views.list_history, name='list_history'),

    path('cash_items/', views.cash_item, name='cash_items'),
    path('cash_detail/<str:pk>/', views.cash_detail, name="cash_detail"),
    path('impriest_level/<str:pk>/', views.impriest_level, name="impriest_level"),
    path('issue_cash/<str:pk>/', views.issue_cash, name="issue_cash"),
    path('receive_cash/<str:pk>/', views.receive_cash, name="receive_cash"),
    path('cash_history/', views.cash_history, name='cash_history'),
]