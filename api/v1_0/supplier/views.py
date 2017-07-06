from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance

from supplier.models import Supplier, Polygon
from api.v1_0.supplier.serializers import SupplierSerializer, PolygonSerializer, PolygonDetailSerializer


class SupplierList(APIView):
    """
    List all suppliers, or create a new supplier.
    """
    def get(self, request, format=None):
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response({"suppliers": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a Supplier
        """
        serializer = SupplierSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"supplier": serializer.data}, status=status.HTTP_201_CREATED)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a supplier instance.
    """
    def get_object(self, pk):
        try:
            return Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier)
        return Response({"supplier": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"supplier": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        supplier = self.get_object(pk)
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PolygonList(APIView):
    """
    List all polygons, or create a new polygon.
    """
    def get(self, request, format=None):
        lat = request.GET.get("lat", "")
        lng = request.GET.get("lng", "")

        polygons = Polygon.objects.filter()

        if lat and lng:
            point = Point(float(lng), float(lat))
            distance = Distance(km=10)
            print point
            print distance
            polygons = polygons.filter(
                point__distance_lt=(point, distance)
            ).distance(point).order_by('distance')

        serializer = PolygonDetailSerializer(polygons, many=True)
        return Response({"polygons": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a Polygon
        """
        serializer = PolygonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print serializer.data
        lat = serializer.validated_data['lat']
        lng = serializer.validated_data['lng']
        point = Point(float(lng), float(lat))
        polygon = Polygon.objects.create(
            supplier=serializer.validated_data['supplier'],
            name=serializer.validated_data['name'],
            price=serializer.validated_data['price'],
            point=point
        )
        serializer = PolygonDetailSerializer(polygon)
        return Response({"polygon": serializer.data}, status=status.HTTP_201_CREATED)
