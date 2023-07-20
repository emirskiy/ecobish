from django.urls import path, include
from project import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('projects', viewset=views.ProjectViewSet, basename='projects')

urlpatterns = [
    path('v1/', include(router.urls)),
]