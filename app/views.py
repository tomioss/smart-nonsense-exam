from django.views import generic

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from app.filters import QuestionTemplateFilter
from app.models import QuestionTemplate
from app.serializers import QuestionTemplateCreateSerializer, QuestionTemplateSerializer, UnityQuestionTemplateSerializer


class QuestionTemplateApiView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsAuthenticated,)
    queryset = QuestionTemplate.objects.all().order_by("id")
    filter_backends = (DjangoFilterBackend,)
    filterset_class = QuestionTemplateFilter

    def get_serializer_class(self):
        if self.action == "create":
            return QuestionTemplateCreateSerializer
        return QuestionTemplateSerializer


class UnityQuestionTemplateApiView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = QuestionTemplate.objects.all().order_by("id").prefetch_related("tags")
    serializer_class = UnityQuestionTemplateSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = QuestionTemplateFilter


class DisplayTemplateView(generic.DetailView):
    model = QuestionTemplate
    template_name = "app/display.html"

