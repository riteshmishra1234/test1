from django.urls import path, re_path
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path('preorder_approval/',views.preorder_approval, name="preorder_approval"),
    path('stock_incentive/',views.stock_incentive, name="stock_incentive"),
]
