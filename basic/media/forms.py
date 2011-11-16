from django import forms
from django.conf import settings
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect
from django.template.defaultfilters import slugify
from basic.media.models import *
from ajax_filtered_fields.forms import AjaxManyToManyField

BASIC_JQUERY_URL = getattr(settings, 'BASIC_JQUERY_URL', 'https://ajax.googleapis.com/ajax/libs/jquery/1.7.0/jquery.min.js')
BASIC_JQUERY_UI_URL = getattr(settings, 'BASIC_JQUERY_UI_URL', 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/jquery-ui.min.js')

ALL_LOOKUPS = (
    ('all', {}),
)

class BaseSetAdminForm(forms.ModelForm):
    class Media:
        js = (
            BASIC_JQUERY_URL,
            '%s/js/SelectBox.js' % settings.ADMIN_MEDIA_PREFIX.rstrip('/'),
            '%s/js/SelectFilter2.js' % settings.ADMIN_MEDIA_PREFIX.rstrip('/'),
            '%s/basic/js/ajax_filtered_fields.js' % settings.STATIC_URL,
        )

class AudioSetAdminForm(BaseSetAdminForm):
    audios = AjaxManyToManyField(Audio, ALL_LOOKUPS, default_index=0, select_related=None)

    class Meta:
        model = Audio


class PhotoSetAdminForm(BaseSetAdminForm):
    photos = AjaxManyToManyField(Photo, ALL_LOOKUPS, default_index=0, select_related=None)

    class Meta:
        model = Photo


class VideoSetAdminForm(BaseSetAdminForm):
    videos = AjaxManyToManyField(Video, ALL_LOOKUPS, default_index=0, select_related=None)

    class Meta:
        model = Video



