import base64
import re
import imghdr

from rest_framework import serializers
from your_snippets.api.models import Snippet, SavedImage, Tag
from django.core.files.base import ContentFile
from rest_framework.filters import OrderingFilter


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        # Check if this is a base64 string
        if isinstance(data, str):
            pattern = re.compile(r'^file_name\:(?P<file_name>[0-9a-z\-]+),data\:.+base64\,(?P<data>.+)$')
            match = pattern.search(data)
            file_name = match.group('file_name')
            data = match.group('data')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except:
                self.fail('invalid_image')

            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)
        else:
            self.fail('invalid_image')

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class SnippetCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        tags_string = validated_data.get('tags')
        for tag in tags_string.split(','):
            tagobj, _ = Tag.objects.get_or_create(name=tag.strip())

        snippet = Snippet.objects.create(**validated_data)
        return snippet


    class Meta:
        model = Snippet
        fields = '__all__'


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('title', 'url', 'content', 'tags', 'images')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    image = Base64ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = SavedImage
        fields = ('image',)


class ImageCreateSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    url = serializers.CharField(max_length=255)

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        url = validated_data.get('url')
        snippet = Snippet.objects.get(url=url)

        for image_data in images_data:
            SavedImage.objects.create(snippet=snippet, **image_data)

        return snippet

    class Meta:
        model = SavedImage
        fields = ('images', 'url',)


class SnippetCreateSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        tags_string = validated_data.get('tags')
        for tag in tags_string.split(','):
            tagobj, _ = Tag.objects.get_or_create(name=tag.strip())

        snippet = Snippet.objects.create(**validated_data)

        for image_data in images_data:
            SavedImage.objects.create(snippet=snippet, **image_data)

        return snippet


    class Meta:
        model = Snippet
        fields = ('title', 'url', 'content', 'tags', 'images')
        #fields = ('created', 'title', 'url', 'content', 'tags', 'images')


class APIImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedImage
        fields = ('image',)


class APIFullSerializer(serializers.ModelSerializer):
    images = APIImageSerializer(many=True)
    filter_backends = (OrderingFilter,)
    ordering = ('-created',)


    class Meta:
        model = Snippet
        fields = ('created', 'title', 'url', 'content', 'tags', 'images')

