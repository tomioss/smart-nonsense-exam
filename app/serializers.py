from rest_framework import serializers

from app.models import QuestionTemplate, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ("name",)


class QuestionTemplateSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = QuestionTemplate
        fields = "__all__"

