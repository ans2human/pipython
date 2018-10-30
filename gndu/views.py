from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Posts, Authors, Project
from django.views.generic import ListView, DetailView

from django.contrib.auth.decorators import login_required
from gndu.forms import ProjectForm


def home(request):
    print(request.user)
    template_name = 'gndu/abc.html'
    return render(request, template_name)

class BlogListView(ListView):
    model = Posts
    # context_object_name = 'sd'  



    # queryset = Posts.objects.all()
    # template_name = 'gndu/blog.html'


# def blog(request):
#     ddd = Posts.objects.all()
#     context = {'sd': ddd,
#                }
#     template_name = 'gndu/blog.html'
#     return render(request, template_name, context)



class BlogDetailView(DetailView):
    model = Posts
    context_object_name = 'blgs'
    template_name = 'gndu/blogpost.html'



# def blogpost(request, pk):
#     blogid = Posts.objects.get(pk=pk)
#     blgs = Posts.objects.all()
#     context = {
#         'blogid': blogid,
#         'blgs': blgs

#     }
#     template_name = 'gndu/blogpost.html'
#     return render(request, template_name, context)


def project(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.save()
        return redirect('/prj')
    return render(request, 'gndu/addproject.html', {'form': form})




def prj(request):
    prj = Project.objects.all()
    template_name = 'gndu/projects.html'
    return render(request, template_name, {'prj' :prj})


















#     prj = get_object_or_404(Project)
#     if request.method == 'POST':
#         form = ProjectForm(request.POST)
#         print(form)
#         if form.is_valid():
#             prj.name = form.cleaned_data['name']
#             prj.startdate = form.cleaned_data['startdate']
#             prj.employee = form.cleaned_data['employee']
#             prj.client = form.cleaned_data['client']
#             prj.description = form.cleaned_data['description']

#             prj.save()
#             redirect('music:index')
#     else:
#         form = ProjectForm()

#     return render(request, 'gndu/addproject.html', {'form': form})


