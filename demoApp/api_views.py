from rest_framework.views import APIView
from .serializers import  UserSerializer
from .models import User
from rest_framework.response import Response

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
