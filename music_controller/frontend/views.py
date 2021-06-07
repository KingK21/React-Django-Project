from django.shortcuts import render

# Create your frontend views here.
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')