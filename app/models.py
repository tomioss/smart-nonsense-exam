from django.db import models
from django.db.models import JSONField


class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class QuestionTemplate(models.Model):
    Question = models.TextField()
    Solution = models.TextField()
    CorrectAnswer = models.TextField()
    Options = JSONField()
    Steps = JSONField(null=True, blank=True)
    ImageUrl = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

