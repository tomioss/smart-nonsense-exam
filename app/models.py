from django.db import models
from django.db.models import JSONField


class QuestionTemplate(models.Model):
    Question = models.TextField()
    Solution = models.TextField()
    CorrectAnswer = models.TextField()
    Options = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

