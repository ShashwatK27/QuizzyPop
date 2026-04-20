from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
import random

from .models import Question, Score
from .serializers import QuestionSerializer, ScoreSerializer, UserSerializer

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)
            
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)
            
        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

class QuestionBatchAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        subject = request.query_params.get('subject', 'machine_learning')
        
        # Get questions for the subject
        qs = list(Question.objects.filter(subject=subject))
        
        if not qs:
            qs = list(Question.objects.all())
            
        random.shuffle(qs)
        
        # Try to return a larger pool for adaptive engine
        qs = qs[:50]
        
        serializer = QuestionSerializer(qs, many=True)
        return Response({subject: serializer.data})

class SubmitScoreAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaderboardAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        subject = request.query_params.get('subject')
        
        if subject:
            scores = Score.objects.filter(subject=subject).order_by('-score', 'time_taken')[:20]
        else:
            scores = Score.objects.all().order_by('-score', 'time_taken')[:20]
            
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)
        
class AnalyticsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        from django.db.models import Avg
        
        scores = Score.objects.filter(user=request.user).order_by('created_at')
        total_games = scores.count()
        average_score = sum(s.score for s in scores) / total_games if total_games > 0 else 0
        best_score = max((s.score for s in scores), default=0)
        
        # Calculate subject performance
        subject_data = scores.values('subject').annotate(avg_accuracy=Avg('accuracy'), avg_score=Avg('score'))
        subject_performance = { item['subject']: round(item['avg_accuracy'], 2) for item in subject_data }
        weakest_subject = min(subject_performance, key=subject_performance.get) if subject_performance else None
        
        # Recent scores for trend line
        recent_scores = scores.order_by('-created_at')[:10]
        recent_trend = [{
            "score": s.score, 
            "accuracy": s.accuracy, 
            "subject": s.subject.replace('_', ' ').title(), 
            "date": s.created_at.strftime("%Y-%m-%d %H:%M")
        } for s in reversed(recent_scores)]

        return Response({
            "total_games": total_games,
            "average_score": round(average_score, 2),
            "best_score": best_score,
            "subject_performance": subject_performance,
            "weakest_subject": weakest_subject,
            "recent_trend": recent_trend
        })
