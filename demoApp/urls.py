from django.urls import  path, include
from rest_framework import routers
from . import views
from . import api_views
app_name = "demoapp"

router = routers.DefaultRouter()
router.register(r'project' , api_views.ProjectView, basename='project'),
urlpatterns=router.urls

urlpatterns += [
    path("projects/list/", api_views.ProjectList.as_view({"get":"list"}), name="project-list"),
    path("createuser/", views.CreateUser.as_view() , name="create-user"),
    path("usercreatesuccess/", views.successfully_user_created ,name="user-create-success"),
    path("createuserfunc", views.createuserFunc, name="create-user-func"),
    path('MyUserView', views.MyUserView.as_view(), name="my-user-view"),
    path("MyUsers", api_views.MyView.as_view() , name="users-list"),
    path("project_pagin/<int:page_no>", views.ProjectPaginView.as_view(), name="project-pagin-view"),
    path("show_time", views.showtime, name="show-time")
]


#{"source_lang": {"source_lang": "en"}, "target_langs": [{"target_lang": "ta"}, {"target_lang": "de"}], "project_name": "demo3", "user": 1}
