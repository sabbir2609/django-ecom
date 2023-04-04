from django.views.generic import TemplateView

from rest_framework import generics

from store.models import Product
from store.serializers import ProductSerializer


class StoreHomeView(TemplateView):
    template_name = "store/index.html"


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
