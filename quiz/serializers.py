from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Score

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    
    class Meta:
        model = Question
        fields = ('id', 'question', 'options', 'correct_index', 'subject', 'difficulty', 'topic', 'explanation')
        
    def get_options(self, obj):
        return [obj.option_a, obj.option_b, obj.option_c, obj.option_d]

class ScoreSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Score
        fields = ('id', 'user', 'username', 'score', 'subject', 'time_taken', 'accuracy', 'created_at')
        read_only_fields = ('user',)
