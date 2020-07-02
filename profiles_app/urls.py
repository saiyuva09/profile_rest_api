from django.urls import path
from profiles_app import views


urlpatterns = [
    path('',views.HellowApiView.as_view()),
]
