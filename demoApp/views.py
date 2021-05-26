from django.shortcuts import render, reverse
from .forms import UserForm, UserForm2
from .models import User
from django.views.generic import CreateView
from django.views import View
from django.http import HttpResponse
import requests, re 
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

class ProjectPaginView(View):
    URL = 'http://127.0.0.1:8000/demoapp/projects/list/%s'
    def get(self, request, page_no):
        res = requests.get(self.URL%f'?page={page_no}') 
        data = res.json() 
        data["next"], data["previous"] = (self.get_page_url(data["next"]), 
                                          self.get_page_url(data["previous"])
                                         )
        return render(request, "pagin-view.html", context=data)

    def get_page_url(self, link):
        page_no = None
        if link:            
            link = re.match( f'({self.URL}%(\?page=.)?)', link).groups()[0]
            page_no = re.sub(self.URL%'(\?page=)?', '', link)
            if page_no:
                page_no = int(page_no)
            else: page_no = 1
        return page_no if not page_no else reverse ('demoapp:project-pagin-view', kwargs={'page_no':page_no})



