from django.shortcuts import redirect, render
from .models import Blog
from django.views.generic import ListView
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login

def home(request):
    blogs = Blog.objects.all().order_by('-created_on')
    return render(request, 'home.html', {'blogs':blogs})

def blog_detail(request, pk, date):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'blog':blog})

def category_filter(request, category):
    blogs = Blog.objects.filter(category=category).order_by('-created_on')
    return render(request, 'category_filter.html', {'blogs':blogs})

class SearchResultsView(ListView):
    model = Blog
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Blog.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(category__icontains=query) | Q(published_status__icontains=query))
        return object_list

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invaid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

