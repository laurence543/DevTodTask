from django.shortcuts import render
from news.models import News
from news.serializers import NewsSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET', 'POST'])
def news_list(request):
    if request.method == 'GET':
        news = News.objects.all()
        news_serializer = NewsSerializer(news, many=True)
        return Response(news_serializer.data)
    elif request.method == 'POST':
        news_serializer = NewsSerializer(data=request.data)
        if news_serializer.is_valid():
            news_serializer.save()
            return Response(news_serializer.data, status=status.HTTP_201_CREATED)
        return Response(news_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def news_detail(request, pk):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        news_serializer = NewsSerializer(news)
        return Response(news_serializer.data)
    elif request.method == 'PUT':
        news_serializer = NewsSerializer(news, data=request.data)
        if news_serializer.is_valid():
            news_serializer.save()
            return Response(news_serializer.data)
        return Response(news_serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
