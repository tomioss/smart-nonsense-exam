from rest_framework import serializers

from app.models import QuestionTemplate


class QuestionTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionTemplate
        fields = "__all__"

