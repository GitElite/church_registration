from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('select_location/', views.select_location, name='select_location'),
    path('manage_database/', views.manage_database, name='manage_database'),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('add_member/', views.add_member, name='add_member'),
    path('delete_rows/', views.delete_rows, name='delete_rows'),
    path('update_member/<int:member_id>/', views.update_member, name='update_member'),
    path('update_rows/', views.update_rows, name='update_rows'),
]