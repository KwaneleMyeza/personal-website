from django.shortcuts import render

# Create your views here.
def projects_home(request):
    return render(request, 'projects/projects.html')
