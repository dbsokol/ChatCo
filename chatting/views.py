from rest_framework import viewsets

from chatting import models
from chatting import serializers


class MessageViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.MessageSerializer
    queryset = models.Message.objects.all().order_by('-timestamp')
