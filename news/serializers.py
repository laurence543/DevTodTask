from news.models import News
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):

    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    link = serializers.CharField(max_length=100)
    votes = serializers.IntegerField()
    author_name = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.link = validated_data.get('link', instance.link)
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.save()
        return instance

    class Meta:
        model = News
        fields = ('pk', 'title', 'link', 'author_name', 'votes', 'created')
