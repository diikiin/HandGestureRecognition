from django.contrib import admin
from django.urls import path

from hand_gesture.views import HandGestureImageAPIView
    # , HandGestureVideoAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/image", HandGestureImageAPIView.as_view()),
    # path("api/video", HandGestureVideoAPIView.as_view())
]
