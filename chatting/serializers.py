from rest_framework import serializers

from chatting import models


class MessageSerializer(serializers.ModelSerializer):

    sender = serializers.SlugRelatedField('name', queryset=models.Sender.objects.all())

    class Meta:
        model = models.Message
        fields = [
            'sender',
            'timestamp',
            'content',
        ]