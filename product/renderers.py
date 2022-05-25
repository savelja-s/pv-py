from django.utils.encoding import smart_str
from rest_framework import renderers


class PlainTextRenderer(renderers.BaseRenderer):
    media_type = 'text/plain'
    format = 'txt'
    charset = 'utf-8'
    render_style = 'binary'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return smart_str(data, encoding=self.charset)
