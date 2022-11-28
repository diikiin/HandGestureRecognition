from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from hand_gesture.views import *

router = routers.DefaultRouter()
router.register(r'hand-gesture', HandGestureViewSet)  # http://127.0.0.1:8000/api/hand-gesture/
router.register(r'translation', TranslationViewSet)  # http://127.0.0.1:8000/api/translation/
from hand_gesture.views import HandGestureImageAPIView
from authenticaiton.views import RegisterView,LoginView,UserView,LogoutView
    # , HandGestureVideoAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/image/", ImageAPIView.as_view()),
    path("api/video/", VideoAPIView.as_view()),
    path("api/", include(router.urls)),
    path("api/image", HandGestureImageAPIView.as_view()),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    # path("api/video", HandGestureVideoAPIView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
