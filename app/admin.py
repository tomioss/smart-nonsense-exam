from django.contrib import admin

from app.models import QuestionTemplate, Tag


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


class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = (
        "id",
        "name",
        "created_at",
        "updated_at",
    )
    readonly_fields=("created_at", "updated_at",)


admin.site.register(QuestionTemplate, QuestionTemplateAdmin)
admin.site.register(Tag, TagAdmin)

