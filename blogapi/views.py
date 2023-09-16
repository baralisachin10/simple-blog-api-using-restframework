from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

# Create your views here.

@api_view(['GET'])
def index(request):
    
    return Response({'success':'The test is successful'})

@api_view(['GET'])
def get_all_post(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many = True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_post(request,id):
    try:
        post = Post.objects.get(id = id)
    except Post.DoesNotExist:
        return Response({'Error':'post not found'},status = 404)
    
    if request.method == 'DELETE':
        post.delete()
        return Response({"success":"post deleted successfully"},status=200)
    
@api_view(['GET'])
def get_post(request,id):
    try:
        post = Post.objects.get(id = id)
    except Post.DoesNotExist:
        return Response({'Error':'post not found'},status=400)
    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data,status=200)
    
@api_view(['PUT'])
def update_post(request,id):
    try:
        post = Post.objects.get(id = id)
    except Post.DoesNotExist:
        return Response({'Error':'post not found'},status=404)
    
    if request.method == 'PUT':
        serializer = PostSerializer(post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        return Response(serializer.errors,stauts=400)
    
