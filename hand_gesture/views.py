import cv2
import numpy as np
from django.forms import model_to_dict
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from hand_gesture.recognition import get_recognition
from .models import HandGesture


class HandGestureImageAPIView(APIView):
    def get(self, request):
        image = request.data["image"]
        data = image.read()
        image = np.asarray(bytearray(data), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return JsonResponse({"text": get_recognition(image)})

    # def post(self, request):
    #     post_new = HandGesture.objects.create(name=request.data['name'])
    #     return Response({'post': model_to_dict(post_new)})

    def post(self, request):
        image = request.data["image"]
        data = image.read()
        image = np.asarray(bytearray(data), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return JsonResponse({"text": get_recognition(image)})

# class HandGestureVideoAPIView(APIView):
    # def get(self, request):

    # def post(self, request):
    #     post = Video


# class HandGestureAPIView(generics.ListAPIView):
#     queryset = HandGesture.objects.all().dates(field_name="name")
#     serializer_class = HandGestureSerializer
