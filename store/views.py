from django.views.generic import TemplateView

from rest_framework.generics import ListAPIView

from store.models import Product
from store.serializers import ProductSerializer


class StoreHomeView(TemplateView):
    template_name = "store/index.html"


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
