from rest_framework import serializers

from product.models import ProductVersion, Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'status',
            'created_at'
        )


class ProductVersionSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.SerializerMethodField(read_only=True)

    def get_product(self, obj: ProductVersion):
        return ProductSerializer(obj.product).data

    class Meta:
        model = ProductVersion
        fields = (
            'id',
            'name',
            'product',
            'created_at'
        )
