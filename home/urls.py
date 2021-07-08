from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('textblog/<int:pk>:<str:date>/', views.blog_detail, name='textblog'),
    path('category/<str:category>/', views.category_filter, name='category_filter'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
]
