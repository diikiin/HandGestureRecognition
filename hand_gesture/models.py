from django.db import models


class HandGesture(models.Model):
    translation_key = models.CharField(max_length=255, db_index=True, null=False, blank=False)
    is_trained = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.translation_key


class Translation(models.Model):
    key = models.CharField(max_length=255, db_index=True, null=False, blank=False)
    value = models.CharField(max_length=255)
    language = models.CharField(max_length=5)

    class Meta:
        unique_together = ('key', 'language',)

    def __str__(self):
        return self.key


class Dataset(models.Model):
    name = models.CharField(max_length=255)
    value = models.FileField(upload_to='models')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


def upload_path(filename):
    return '/'.join(['media', filename])


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(blank=True, null=True, upload_to=upload_path)

    def __str__(self):
        return self.title
