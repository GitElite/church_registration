from django.urls import path
from django.urls import re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('select_zone/', views.select_zone, name='select_zone'),
    path('manage_database/', views.manage_database, name='manage_database'),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('add_member/', views.add_member, name='add_member'),
    path('delete_rows/', views.delete_rows, name='delete_rows'),
    path('update_member/<int:member_id>/', views.update_member, name='update_member'),
    re_path(r'^update_member/(?P<member_id>[0-9]+)/?$', views.update_member, name='update_member'),
    path('update_rows/', views.update_rows, name='update_rows'),
    path('logout_view/', views.logout_view, name='logout_view'),
]
