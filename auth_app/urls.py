from django.urls import path
from . import views

urlpatterns = [
    # path('mytoken/', views.login_set_cookie),
    path('login/', views.UserLogin.as_view()),
    path('registration/', views.UserRegistration.as_view()),
    path('admin/permissions/', views.AdminPermissions.as_view()),
    path('logout/', views.LogoutUser.as_view()),
    path('get/customer/', views.CustomerGetSearch.as_view()),
    # path('user/', views.UserInfo.as_view()),
]
