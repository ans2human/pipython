from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts, Authors

def home(request):
    print(request.user)
    template_name = 'gndu/abc.html'
    return render(request, template_name)


def blog(request):
    ddd = Posts.objects.all()
    context = {'sd':ddd,
               }
    template_name = 'gndu/blog.html'
    return render(request, template_name, context)


def blogpost(request, pk):
    blogid = Posts.objects.get(pk=pk)
    blgs = Posts.objects.all()
    context = {
        'blogid': blogid,
        'blgs' : blgs

    }
    template_name = 'gndu/blogpost.html'
    return render(request, template_name, context)