from django.urls import path

from rest_framework.routers import DefaultRouter

from app.views import QuestionTemplateApiView, DisplayTemplateView


app_name = "app"

router = DefaultRouter()
router.register("questions", QuestionTemplateApiView, basename="questions")

urlpatterns = router.urls + [
    path("display/<int:pk>/", DisplayTemplateView.as_view(), name="display-template"),
]

