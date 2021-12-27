from os import name
from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog-home'),
    path('single/', single_view, name='blog-single'),
    path('<str:fname>/<str:lname>/post-<int:number>/', test_view, name='test'),
]