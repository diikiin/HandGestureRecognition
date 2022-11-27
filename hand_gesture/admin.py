from django.contrib import admin

from .models import HandGesture, Video, Translation

admin.site.register(HandGesture)
# admin.site.register(Video)
admin.site.register(Translation)
