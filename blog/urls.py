from django.urls import path
from . import views

urlpatterns = [
 path('',views.blog_app,name='blog_app'),
 path('<int:blog_id>/',views.detail,name='blog_id'),
]