from django.shortcuts import render
from django.http import JsonResponse

#third party imports
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics

class TestView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self,*args,**kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self,request,*args,** kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PostView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self,request,*args,**kwargs):
        return self.list(self, request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

class PostCreateView(mixins.ListModelMixin,generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self,request,*args,**kwargs):
        return self.list(self, request, *args, **kwargs)

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
