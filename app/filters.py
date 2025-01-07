from django_filters import rest_framework as filters

from app.models import QuestionTemplate


class QuestionTemplateFilter(filters.FilterSet):
    tags = filters.CharFilter(field_name="tags__name", lookup_expr="contains")

    class Meta:
        model = QuestionTemplate
        fields = (
            "Question",
            "Solution",
            "tags"
        )

