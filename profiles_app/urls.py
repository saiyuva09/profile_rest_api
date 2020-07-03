from django.urls import path, include
from profiles_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('h-viewset', views.HelloViewSet, base_name='hellow_view')
router.register('profiles',views.UserProfileViewSet)

urlpatterns = [
    path('hello', views.HellowApiView.as_view()),
    path('', include(router.urls)),
]
