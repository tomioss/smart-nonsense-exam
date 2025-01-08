from django.urls import path

from rest_framework.routers import DefaultRouter

from app.views import QuestionTemplateApiView, DisplayTemplateView, UnityQuestionTemplateApiView


app_name = "app"

router = DefaultRouter()
router.register("questions", QuestionTemplateApiView, basename="questions")
router.register("unity/questions", UnityQuestionTemplateApiView, basename="unity-questions")

urlpatterns = router.urls + [
    path("display/<int:pk>/", DisplayTemplateView.as_view(), name="display-template"),
]

