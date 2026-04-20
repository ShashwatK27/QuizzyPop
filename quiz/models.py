from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    SUBJECT_CHOICES = [
        ('machine_learning', 'Machine Learning'),
        ('operating_systems', 'Operating Systems'),
        ('dbms', 'DBMS'),
        ('software_engineering', 'Software Engineering'),
        ('daa', 'DAA'),
    ]
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    question = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_index = models.IntegerField(
        help_text="0=A, 1=B, 2=C, 3=D"
    )
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    topic = models.CharField(max_length=100, blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"[{self.subject.upper()}] {self.question[:60]}"


class Score(models.Model):
    SUBJECT_CHOICES = [
        ('machine_learning', 'Machine Learning'),
        ('operating_systems', 'Operating Systems'),
        ('dbms', 'DBMS'),
        ('software_engineering', 'Software Engineering'),
        ('daa', 'DAA'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    time_taken = models.IntegerField(default=0, help_text="Time taken in seconds")
    accuracy = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username} — {self.score} ({self.subject})"
