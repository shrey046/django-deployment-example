from django.shortcuts import render
from django.http import HttpResponse
# from .models import User
from .forms import NewUserForm

# Create your views here.

def index(request):
    my_dict = {'insert_me' : 'Hello, Changed !'}
    return render(request,'first_app/index.html',context=my_dict)

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit= True)
            return index(request)

        else:
            print("Error Form Invalid ")

    return render(request,'first_app/user.html',{'form':form})
