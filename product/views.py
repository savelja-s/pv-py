from django.http import Http404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication
from product.models import ProductVersion
from product.renderers import PlainTextRenderer
from product.serializers import ProductVersionSerializer


class LatestProductVersion(APIView):
    authentication_classes: authentication.JWTTokenUserAuthentication
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, product_id: int):
        q = ProductVersion.objects.filter(product__id=product_id)
        if not q.count():
            raise Http404
        version = q.latest('created_at')
        serializer = ProductVersionSerializer(version, context={'request': request})
        return Response(serializer.data)


class ViewProductVersionFile(APIView):
    authentication_classes: authentication.JWTTokenUserAuthentication
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [PlainTextRenderer]

    def get(self, request, product_id: int, version_id: int):
        try:
            version = ProductVersion.objects.filter(product__id=product_id).get(pk=version_id)
        except ProductVersion.DoesNotExist:
            raise Http404
        return Response(version.file.read())
