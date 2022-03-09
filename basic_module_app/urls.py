from rest_framework.routers import DefaultRouter

from . import views
from django.urls import path

router = DefaultRouter()
router.register("company", views.CompanyCRUD, basename="basic-module-company")
router.register("category", views.CategoryCRUD, basename="basic-module-category")
router.register("type", views.TypeCRUD, basename="basic-module-type")
router.register("color", views.ColorCRUD, basename="basic-module-color")
router.register("bank", views.BankCRUD, basename="basic-module-bank")
router.register("route", views.RouteCRUD, basename="basic-module-route")
router.register("godown", views.GodownCRUD, basename="basic-module-godown")
router.register("product/init", views.ProductInitCRUD, basename="basic-module-product-init")
# other
# router.register("product", views.ProductCRUD, basename="product")
# router.register("product/info", views.ProductInfoCRUD, basename="product_info")
# router.register("admin/designation", views.AdminDesignationCRUD, basename="designation")

urlpatterns = [
    # Company crud
    # path("all/supplier/",views.AllSupplier.as_view()),
]
urlpatterns += router.urls
