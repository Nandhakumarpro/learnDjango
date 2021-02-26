from django.db import models
from django.contrib.auth.models import User as DjUser

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, null=False, unique=True )
    password = models.CharField(max_length=20,)#max_length=200, null= True )

class Post(models.Model):
    title = models.CharField(max_length=20,null=False)
    desc = models.CharField(max_length=1000, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Project(models.Model):
    project_name = models.CharField(max_length=20, null= False)
    user = models.ForeignKey(DjUser, on_delete= models.CASCADE)

lang_choices = (
    ("en", "English"),
    ("ta", "Tamil"),
    ("de", "German")
)

class SourceLang(models.Model):
    source_lang = models.CharField(choices=lang_choices ,max_length=20, null= False )
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

class TargetLang(models.Model):
    target_lang = models.CharField(choices =lang_choices,max_length=20, null= False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
