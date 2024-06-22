from django.urls import path,include
from rest_framework import routers 
from Api_user import views

router=routers.DefaultRouter()
router.register(r'usuario',views.UserViewSet)


urlpatterns = [
    path('',include(router.urls))
]
