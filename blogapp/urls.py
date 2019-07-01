from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
import blogapp.views


urlpatterns =[
    path('/home', blogapp.views.home, name='home'),
    path('', blogapp.views.post, name='post'),
    path('post/<int:post_id>/', blogapp.views.detail, name='detail'),
    path('post/new/', blogapp.views.new, name='new'),
    path('post/create/', blogapp.views.create, name='create'),
    path('delete/<int:post_id>/', blogapp.views.delete, name='delete'),
]