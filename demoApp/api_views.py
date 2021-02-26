from rest_framework.views import APIView
from .serializers import  (
    UserSerializer, ProjectSerializer, ProjectListSerializer,
    SourceLangSerializer, TargetLangSerializer)
from .models import User,Project, SourceLang, TargetLang
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import JsonResponse

class MyView(APIView):
    def get(self,request):
        objs = User.objects.all()
        serializer = UserSerializer( objs ,many = True )
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status = 201)

class ProjectList(viewsets.ModelViewSet):
    serializer_class = ProjectListSerializer
    queryset = Project.objects.all()

class ProjectView(viewsets.ViewSet):
    def create(self, request):
        ps = ProjectSerializer( data = request.data)
        if ps.is_valid(raise_exception= True):
            ps.save()# Custom save function call in serializer
            return Response (ps.data, status=201)
    def retrieve(self, request, pk):
        queryset = Project.objects.all()
        project = get_object_or_404(queryset, pk=pk)
        source_lang = SourceLang.objects.filter( project=project ).first()
        target_langs = TargetLang.objects.filter(project=project).all()
        project_serializer = ProjectSerializer( project )
        sr_ = SourceLangSerializer(source_lang,many= False)
        tr_ = TargetLangSerializer(target_langs, many=True)
        return Response ({"project":project_serializer.data, "source":sr_.data ,"target":tr_.data })
