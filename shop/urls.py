from django.urls import path
from shop.views import dashboard

urlpatterns = [
   path("",dashboard,name="dashboard"),
]