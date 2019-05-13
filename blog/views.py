from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':posts})

def category(requets, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(requets, "blog/category.html", { 'category':category})
