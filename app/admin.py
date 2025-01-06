from django.contrib import admin

from app.models import QuestionTemplate


class QuestionTemplateAdmin(admin.ModelAdmin):
    model = QuestionTemplate
    list_display = (
        "id",
        "Question",
        "Solution",
        "CorrectAnswer",
        "Options",
        "created_at",
        "updated_at",
    )
    readonly_fields=("created_at", "updated_at",)

admin.site.register(QuestionTemplate, QuestionTemplateAdmin)

