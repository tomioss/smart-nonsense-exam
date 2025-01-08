from rest_framework import serializers

from app.models import QuestionTemplate, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ("id", "name",)


class QuestionTemplateSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = QuestionTemplate
        fields = "__all__"


class QuestionTemplateCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionTemplate
        fields = "__all__"


class UnityQuestionTemplateSerializer(serializers.ModelSerializer):
    Tags = serializers.SerializerMethodField()

    class Meta:
        model = QuestionTemplate
        fields = (
            "Question",
            "Solution",
            "CorrectAnswer",
            "Options",
            "Steps",
            "ImageUrl",
            "Tags"
        )

    def get_Tags(self, instance):
        return [tag.name for tag in instance.tags.all()]

