from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Post
from .serializers import PostSerializer

# Create your views here.
class PostView(APIView):
    def get(self, request):
        data = Post.objects.all()
        serializer = PostSerializer(data, many = True)
        
        return Response(serializer.data)

    # def post(self, request):
    #     datas = request.data
    #     print(datas)

    #     serializer = PostSerializer(data=datas)

    #     if serializer.is_valid():
    #         serializer.save() 
    #         return Response({"message": "Data has been saved."})

    #     return Response({"message": "Submited data is found."})


