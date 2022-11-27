from rest_framework import serializers

from .models import Image, Video, HandGesture, Translation


class HandGestureSerializer(serializers.Serializer):
    translation_key = serializers.CharField(max_length=255, required=False)
    is_trained = serializers.BooleanField(required=False)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    def update(self, instance, validated_data):
        instance.is_trained = validated_data.get("is_trained", instance.is_trained)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.save()
        return instance

    def create(self, validated_data):
        return HandGesture.objects.create(**validated_data)


class TranslationSerializer(serializers.Serializer):
    key = serializers.CharField(max_length=255)
    value = serializers.CharField(max_length=255)
    language = serializers.CharField(max_length=5)

    def update(self, instance, validated_data):
        instance.value = validated_data.get("value", instance.value)
        instance.save()
        return instance

    def create(self, validated_data):
        return Translation.objects.create(**validated_data)

# class HandGestureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HandGesture
#         fields = ("translation_key", "is_trained", "time_create", "time_update")

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ['video']
