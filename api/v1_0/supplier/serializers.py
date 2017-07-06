from rest_framework import serializers

from supplier.models import Supplier, Polygon


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class PolygonSerializer(serializers.ModelSerializer):
    lat = serializers.CharField()
    lng = serializers.CharField()

    class Meta:
        model = Polygon
        exclude = ("point", )


class PolygonDetailSerializer(serializers.ModelSerializer):
    lng = serializers.SerializerMethodField()
    lat = serializers.SerializerMethodField()

    class Meta:
        model = Polygon
        exclude = ("point", )

    def get_lng(self, obj):
        if obj.point:
            return obj.point.get_x()

    def get_lat(self, obj):
        if obj.point:
            return obj.point.get_y()
