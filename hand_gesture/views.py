import cv2
import numpy as np
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from hand_gesture.recognition import get_recognition
from .models import Translation, HandGesture
from .serializers import HandGestureSerializer, TranslationSerializer


class HandGestureImageAPIView(APIView):
    def post(self, request):
        image = request.data["image"]
        data = image.read()
        image = np.asarray(bytearray(data), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        text = Translation.objects.get(key=get_recognition(image), language=request.data["language"]).value
        return Response({"data": text})


# class HandGestureAPIView(APIView):
#     @staticmethod
#     def get_object(pk):
#         if not pk:
#             return Response({"error": "Id can't be null"})
#         try:
#             return HandGesture.objects.get(pk=pk)
#         except:
#             return Response({"error": "Hand gesture with id=" + str(pk) + " not found"},
#                             status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request):
#         return Response({"data": HandGestureSerializer(HandGesture.objects.all(), many=True).data})
#
#     def post(self, request):
#         translations = request.data["translations"]
#         key = translations["en"].replace(" ", "").lower()
#
#         translations = [{"key": key, "value": translations["kz"], "language": "kz"},
#                         {"key": key, "value": translations["en"], "language": "en"},
#                         {"key": key, "value": translations["ru"], "language": "ru"}]
#         translation_serializer = TranslationSerializer(data=translations, many=True)
#         translation_serializer.is_valid(raise_exception=True)
#         translation_serializer.save()
#
#         hand_serializer = HandGestureSerializer(data={"translation_key": key})
#         hand_serializer.is_valid(raise_exception=True)
#         hand_serializer.save()
#
#         return Response({"data": {"gesture": hand_serializer.data,
#                                   "translations": translation_serializer.data}},
#                         status=status.HTTP_201_CREATED)
#
#     def put(self, request, *args, **kwargs):
#         serializer = HandGestureSerializer(data=request.data,
#                                            instance=self.get_object(kwargs.get("pk", None)))
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data)
#
#     def delete(self, request, *args, **kwargs):
#         return Response(self.get_object(kwargs.get("pk", None)).delete())


class TranslationAPIView(APIView):
    def get(self, request):
        return Response({"data": TranslationSerializer(Translation.objects.all(), many=True).data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Id can't be null"})

        try:
            instance = HandGesture.objects.get(pk=pk)
        except:
            return Response({"error": "Translation with id=" + str(pk) + " not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = TranslationSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data": serializer.data})


class HandGestureViewSet(viewsets.ModelViewSet):
    queryset = HandGesture.objects.all()
    serializer_class = HandGestureSerializer

    def create(self, request, *args, **kwargs):
        translations = request.data["translations"]
        key = translations["en"].replace(" ", "").lower()

        translations = [{"key": key, "value": translations["kz"], "language": "kz"},
                        {"key": key, "value": translations["en"], "language": "en"},
                        {"key": key, "value": translations["ru"], "language": "ru"}]
        translation_serializer = TranslationSerializer(data=translations, many=True)
        translation_serializer.is_valid(raise_exception=True)
        translation_serializer.save()

        hand_serializer = HandGestureSerializer(data={"translation_key": key})
        hand_serializer.is_valid(raise_exception=True)
        hand_serializer.save()

        return Response({"data": {"gesture": hand_serializer.data,
                                  "translations": translation_serializer.data}},
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        try:
            hand_gesture = HandGesture.objects.get(pk=pk)
            Translation.objects.filter(key=hand_gesture.translation_key).delete()
            return Response({"message": "Hand gesture with id=" + str(pk) + " was deleted"})
        except HandGesture.DoesNotExist:
            return Response({"error": "Hand gesture with id=" + str(pk) + " not found"},
                            status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=False)
    def train(self, request):
        trained = HandGesture.objects.filter(is_trained=request.GET.get("is_trained", None))
        page = self.paginate_queryset(trained)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(trained, many=True)
        return Response(serializer.data)


# @api_view(('GET',))
# @renderer_classes((JSONRenderer,))
# def get_is_trained(request):
#     print(request.data["is_trained"])
#     return Response({"data": HandGestureSerializer(
#         HandGesture.objects.filter(is_trained=request.data["is_trained"]), many=True).data})
