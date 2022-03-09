from . import views
from django.urls import path

urlpatterns = [
    # Company crud
    path("purchase/order/", views.PurchaseOrderView.as_view()),
    # path("sales/order/", views.SalesOrderView.as_view()),
    # path("sr/visit/", views.SRVisitView.as_view()),
]
