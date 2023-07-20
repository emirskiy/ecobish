from django.urls import path, include
from new import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('news', viewset=views.NewViewSet, basename='news')

urlpatterns = [
    path('v1/', include(router.urls))
]