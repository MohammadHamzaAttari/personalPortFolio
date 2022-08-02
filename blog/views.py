from django.shortcuts import render
from .models import Blog

def blog_app(request):
    data=Blog.objects.all()
    return render(request,'blog/blog.html',{'model_data':data})
def detail(request,blog_id):
    return render(request,'blog/detail.html',{'id':blog_id})