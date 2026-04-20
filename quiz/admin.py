from django.contrib import admin
from .models import Question, Score

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'subject', 'difficulty', 'correct_index')
    list_filter = ('subject', 'difficulty')
    search_fields = ('question', 'topic')

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'subject', 'time_taken', 'accuracy', 'created_at')
    list_filter = ('subject',)
    ordering = ('-score',)
