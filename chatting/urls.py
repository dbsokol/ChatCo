from django.urls import path, include
from rest_framework import routers

from chatting import views


router = routers.DefaultRouter()
router.register("messages", views.MessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
