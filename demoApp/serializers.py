from .models import User, Project, SourceLang, TargetLang, lang_choices
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = "__all__"

class SourceLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceLang
        fields = ("source_lang", )

class TargetLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetLang
        fields = ('target_lang', )

class ProjectListSerializer(serializers.ModelSerializer):
    project_detail = serializers.HyperlinkedIdentityField(read_only= True,view_name='demoapp:project-detail',lookup_field="pk")
    class Meta:
        model = Project
        fields = ("project_name", "project_detail")

class ProjectSerializer(serializers.ModelSerializer):
    source_lang = SourceLangSerializer( required = False )
    target_langs = TargetLangSerializer(many = True , required = False)

    class Meta:
        model = Project
        fields = "__all__"
        extra_kwargs = {
            "source_lang":{"write_only":True},
            'target_langs':{"write_only":True}
        }
    def create(self, *args, **kwargs):
        source_lang = self.validated_data.pop("source_lang")
        target_langs = self.validated_data.pop("target_langs")
        project = Project.objects.create(**self.validated_data)
        SourceLang.objects.create( **dict(**source_lang,project=project ))
        for target_lang in target_langs:
            TargetLang.objects.create(**target_lang, project=project )
        return project
