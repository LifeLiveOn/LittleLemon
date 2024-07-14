from django.urls import path, include
from .views import index
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'',views.UserViewSet)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('user/', include(router.urls)),
    path('home/',index, name='index'),
    path('menu/',views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]