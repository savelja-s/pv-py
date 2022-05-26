from django.core.files import File
from rest_framework import renderers


class PlainTextRenderer(renderers.BaseRenderer):
    media_type = 'text/plain'
    format = 'txt'
    render_style = 'binary'

    def render(self, data: File, accepted_media_type=None, renderer_context=None):
        return data.read()
