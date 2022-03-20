from . import views
from django.urls import path

urlpatterns = [
    # Company crud
    path("purchase/order/", views.PurchaseOrderView.as_view()),
    path("search/product/",views.SearchProductView.as_view()),
    path("sales/order/",views.SalesOrderView.as_view()),
    path("sr/visit/<int:product_detail_id>/",views.sr_visit_view),
    path("sales/return/",views.SalesReturnView.as_view()),
    # path("sales/order/", views.SalesOrderView.as_view()),
    # path("sr/visit/", views.SRVisitView.as_view()),
]
