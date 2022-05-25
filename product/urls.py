from django.urls import path

from product import views

urlpatterns = [
    path(
        'product/<int:product_id>/versions/latest/',
        views.LatestProductVersion.as_view(),
        name='api_product_versions_latest'
    ),
    path(
        'product/<int:product_id>/versions/<int:version_id>/file/',
        views.ViewProductVersionFile.as_view(),
        name='api_product_versions_file_view'
    ),
]
