from django.views import generic

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from app.models import QuestionTemplate
from app.serializers import QuestionTemplateSerializer


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
    serializer_class = QuestionTemplateSerializer


class DisplayTemplateView(generic.DetailView):
    model = QuestionTemplate
    template_name = "app/display.html"

