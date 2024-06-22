from django.urls import path,include
from rest_framework import routers 
from Api_products import views

router=routers.DefaultRouter()
router.register(r'products',views.ProductsViewSet)

urlpatterns = [
    path('', include(router.urls))
]