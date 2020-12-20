from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True)
    author_name = serializers.CharField(max_length=150)
    content = serializers.CharField(max_length=250)

    def create(self, validated_data):
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author_name = validated_data.get('name', instance.author_name)
        instance.content = validated_data.get('description', instance.content)
        instance.save()
        return instance
