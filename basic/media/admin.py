from django.conf import settings
from django.contrib import admin
from basic.media.forms import *
from basic.media.models import *
from sorl.thumbnail import get_thumbnail

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
    list_display = ['thumb', 'title']
    prepopulated_fields = {'slug': ('title',)}

    def thumb(self, obj):
        if obj.photo:
            im = get_thumbnail(obj.photo, '100x100', crop='center', quality=99)
            return u'<img src="%s/%s" width="%s" />' % (settings.MEDIA_URL, im.url.lstrip('/'), im.width)
        else:
            return u'No Image'

    thumb.short_description = 'Thumbnail'
    thumb.allow_tags = True

admin.site.register(Photo, PhotoAdmin)


class VideoSetAdmin(admin.ModelAdmin):
    form = VideoSetAdminForm
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(VideoSet, VideoSetAdmin)


class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Video, VideoAdmin)
