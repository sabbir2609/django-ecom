from django.urls import path

from . import views

app_name = "store"
urlpatterns = [
    path("", views.StoreHomeView.as_view(), name="index"),
    path("api/", views.ProductListView.as_view(), name="store_home"),
]
