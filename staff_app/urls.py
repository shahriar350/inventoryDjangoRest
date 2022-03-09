from rest_framework.routers import DefaultRouter

from . import views
from django.urls import path

router = DefaultRouter()

# other
router.register("admin/designation", views.AdminDesignationCRUD, basename="admin-designation")
router.register("employee", views.EmployeeCRUD, basename="employee")
router.register("bank", views.BankCRUD, basename="bank")
# router.register("supplier", views.SupplierCRUD, basename="supplier")
# router.register("product/info", views.ProductInfoCRUD, basename="product_info")
# router.register("admin/designation", views.AdminDesignationCRUD, basename="designation")

urlpatterns = [
    # Company crud
    path("supplier/", views.SupplierCRUD.as_view()),
]
urlpatterns += router.urls
