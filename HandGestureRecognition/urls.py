from django.contrib import admin
from django.urls import path

from hand_gesture.views import HandGestureImageAPIView
from authenticaiton.views import RegisterView,LoginView,UserView,LogoutView
    # , HandGestureVideoAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/image", HandGestureImageAPIView.as_view()),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    # path("api/video", HandGestureVideoAPIView.as_view())
]
