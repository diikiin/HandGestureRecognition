from django.contrib import admin
from django.urls import path, include

from hand_gesture.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hand-gesture', HandGestureViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/image/", HandGestureImageAPIView.as_view()),
    path("api/is-trained/", get_is_trained),
    path("api/", include(router.urls)),  # http://127.0.0.1:8000/api/hand-gesture/
    # path("api/video", HandGestureVideoAPIView.as_view()),
    # path("api/hand-gesture/", HandGestureAPIView.as_view()),
    # path("api/hand-gesture/", HandGestureViewSet.as_view({"get": "list"})),
    # # path("api/hand-gesture/<int:pk>/", views.HandGestureAPIView.as_view()),
    # path("api/hand-gesture/<int:pk>/", HandGestureViewSet.as_view({"put": "update"})),
    # # path("api/hand-gesture/all", views.HandGestureAPIViewGet.as_view()),

]
