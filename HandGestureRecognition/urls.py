from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from hand_gesture.views import *

router = routers.DefaultRouter()
router.register(r'hand-gesture', HandGestureViewSet)  # http://127.0.0.1:8000/api/hand-gesture/
router.register(r'translation', TranslationViewSet)  # http://127.0.0.1:8000/api/translation/

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/image/", ImageAPIView.as_view()),
    path("api/video/", VideoAPIView.as_view()),
    path("api/", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
