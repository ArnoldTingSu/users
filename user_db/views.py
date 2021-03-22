from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.

def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request,'all_users.html', context)

def delete_user(request, user_id):
    delete_id = User.objects.get(id=user_id)
    delete_id.delete()
    return redirect('/')

def create_user(request):
    print(request.POST)
    print(request.POST['name'])
    User.objects.create(name=(request.POST['name']), email=(request.POST['email']), age=request.POST['age'])
    return redirect('/')