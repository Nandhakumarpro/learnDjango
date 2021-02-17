from django.urls import  path, include
from . import views
app_name = "demoapp"

urlpatterns = [
    path("createuser/", views.CreateUser.as_view() , name="create-user"),
    path("usercreatesuccess/", views.successfully_user_created ,name="user-create-success"),
    path("createuserfunc", views.createuserFunc, name="create-user-func"),
    path('MyUserView', views.MyUserView.as_view(), name="my-user-view"),
]
