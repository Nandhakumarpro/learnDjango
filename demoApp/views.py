from django.shortcuts import render, reverse
from .forms import UserForm, UserForm2
from .models import User
from django.views.generic import CreateView
from django.views import View
from django.http import HttpResponse
# Create your views here.

def successfully_user_created(request):
    return HttpResponse("<h3>New User Created Successfully</h3>")

class CreateUser(CreateView):

    model = User
    form_class = UserForm
    template_name = "create-user.html"
    # t
    def get_success_url(self):
        return  reverse("demoapp:user-create-success")


def createuserFunc( request) :
    form = UserForm2()
    if request.method == 'POST':
        form = UserForm2(request.POST or None )
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create(**data)
            return HttpResponse("<h3>successfully_user_created</h3>")
    return render(request,"create-user.html", {"form":form} )

class MyUserView(View):
    def get(self,request):
        form = UserForm2()
        return render(request,"create-user.html", {"form":form} )
    def post(self,request):
        form = UserForm2(request.POST or None )
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create(**data)
            return HttpResponse("<h3>successfully_user_created</h3>")
        return render(request,"create-user.html", {"form":form} )
