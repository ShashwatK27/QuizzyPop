from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
import random

from .models import Question, Score
from .serializers import QuestionSerializer, ScoreSerializer, UserSerializer

SUBJECT_LABELS = dict(Question.SUBJECT_CHOICES)
SUBJECT_ALIASES = {
    key: key for key in SUBJECT_LABELS
}
SUBJECT_ALIASES.update({
    label.lower().replace(' ', '_'): key
    for key, label in SUBJECT_LABELS.items()
})
SUBJECT_ALIASES.update({
    'ml': 'machine_learning',
    'machinelearning': 'machine_learning',
    'os': 'operating_systems',
    'operating_system': 'operating_systems',
    'database_management_system': 'dbms',
    'se': 'software_engineering',
    'software_engineer': 'software_engineering',
    'algorithms': 'daa',
})


def normalize_subject(value, default=None):
    if value is None or value == '':
        return default

    normalized = str(value).strip().lower().replace('-', '_').replace(' ', '_')
    return SUBJECT_ALIASES.get(normalized)


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
        subject = normalize_subject(request.query_params.get('subject'), default='machine_learning')
        if not subject:
            return Response(
                {
                    "error": "Invalid subject.",
                    "available_subjects": list(SUBJECT_LABELS.keys()),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        # Return only questions for the requested subject. Do not fall back to all
        # subjects, because that mixes categories in the quiz UI.
        qs = list(Question.objects.filter(subject=subject))
            
        random.shuffle(qs)
        
        # Try to return a larger pool for adaptive engine
        qs = qs[:50]
        
        serializer = QuestionSerializer(qs, many=True)
        return Response({
            "subject": subject,
            "questions": serializer.data,
            subject: serializer.data,
        })

class SubmitScoreAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data.copy()
        subject = normalize_subject(data.get('subject'))
        if not subject:
            return Response(
                {
                    "subject": ["Invalid subject."],
                    "available_subjects": list(SUBJECT_LABELS.keys()),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        data['subject'] = subject
        serializer = ScoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaderboardAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        subject = request.query_params.get('subject')
        
        if subject:
            subject = normalize_subject(subject)
            if not subject:
                return Response(
                    {
                        "error": "Invalid subject.",
                        "available_subjects": list(SUBJECT_LABELS.keys()),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            scores = Score.objects.filter(subject=subject).order_by('-score', 'time_taken')[:10]
        else:
            scores = Score.objects.all().order_by('-score', 'time_taken')[:10]
            
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
