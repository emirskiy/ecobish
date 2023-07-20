from django.urls import path, include
from event import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('events', viewset=views.EventViewSet, basename='events')

urlpatterns = [
    path('v1/', include(router.urls))
]