from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.files import FieldFile
from django.template.defaultfilters import slugify

STATUS_ACTIVE = 'active'
STATUS_DEACTIVE = 'deactive'

STATUSES = (
    (STATUS_ACTIVE, 'Active'),
    (STATUS_DEACTIVE, 'Deactive'),
)


class Product(models.Model):
    name: str = models.CharField(max_length=250, unique=True)
    status = models.CharField(max_length=15, choices=STATUSES, default=STATUS_ACTIVE)
    user = models.ForeignKey(User, related_name='products', on_delete=models.DO_NOTHING)
    priority: int = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductVersion(models.Model):
    def upload_file(self, filename):
        return f'var/files/{slugify(self.product.name)}/{slugify(self.name)}'

    name: str = models.CharField(max_length=30, unique=True)
    product = models.ForeignKey(
        Product,
        related_name='versions',
        on_delete=models.DO_NOTHING,
    )
    file: FieldFile = models.FileField(upload_to=upload_file)
    user = models.ForeignKey(User, related_name='product_versions', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_versions'
        verbose_name = 'ProductVersion'
        verbose_name_plural = 'ProductVersions'
        ordering = ['-created_at', ]
