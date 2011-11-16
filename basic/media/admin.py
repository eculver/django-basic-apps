from django.conf import settings
from django.contrib import admin
from basic.media.forms import *
from basic.media.models import *

class AudioSetAdmin(admin.ModelAdmin):
    form = AudioSetAdminForm
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(AudioSet, AudioSetAdmin)


class AudioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Audio, AudioAdmin)


class PhotoSetAdmin(admin.ModelAdmin):
    form = PhotoSetAdminForm
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(PhotoSet, PhotoSetAdmin)


class PhotoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Photo, PhotoAdmin)


class VideoSetAdmin(admin.ModelAdmin):
    form = VideoSetAdminForm
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(VideoSet, VideoSetAdmin)


class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Video, VideoAdmin)
