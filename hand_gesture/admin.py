from django.contrib import admin

from .models import HandGesture, Video, Translation

admin.site.register(HandGesture)
admin.site.register(Translation)
admin.site.register(Video)
