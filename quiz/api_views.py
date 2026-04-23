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

# Fixed API dataset for automation suites such as Katalon.
# This path is used only when the URL includes ?test=true.
TEST_MODE_QUESTIONS = [
    {
        "id": "test-1",
        "question": "TEST MODE: Which data structure uses FIFO order?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "correct_index": 1,
        "difficulty": "easy",
        "topic": "Automation Test",
        "explanation": "A queue follows First In, First Out order.",
    },
    {
        "id": "test-2",
        "question": "TEST MODE: What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Core Processing Utility"],
        "correct_index": 1,
        "difficulty": "easy",
        "topic": "Automation Test",
        "explanation": "CPU stands for Central Processing Unit.",
    },
    {
        "id": "test-3",
        "question": "TEST MODE: Which language is commonly used for database queries?",
        "options": ["HTML", "SQL", "CSS", "XML"],
        "correct_index": 1,
        "difficulty": "medium",
        "topic": "Automation Test",
        "explanation": "SQL is commonly used to query relational databases.",
    },
    {
        "id": "test-4",
        "question": "TEST MODE: Which algorithmic complexity is fastest here?",
        "options": ["O(n2)", "O(n log n)", "O(n)", "O(1)"],
        "correct_index": 3,
        "difficulty": "medium",
        "topic": "Automation Test",
        "explanation": "O(1) is constant time and is fastest among these choices.",
    },
    {
        "id": "test-5",
        "question": "TEST MODE: Which normal form removes transitive dependency?",
        "options": ["1NF", "2NF", "3NF", "BCNF"],
        "correct_index": 2,
        "difficulty": "medium",
        "topic": "Automation Test",
        "explanation": "Third Normal Form removes transitive dependencies.",
    },
    {
        "id": "test-6",
        "question": "TEST MODE: Which scheduling algorithm uses a time quantum?",
        "options": ["FCFS", "SJF", "Round Robin", "Priority Scheduling"],
        "correct_index": 2,
        "difficulty": "medium",
        "topic": "Automation Test",
        "explanation": "Round Robin uses a fixed time quantum for each process.",
    },
    {
        "id": "test-7",
        "question": "TEST MODE: Which machine learning type uses labeled data?",
        "options": ["Unsupervised", "Supervised", "Reinforcement", "Clustering"],
        "correct_index": 1,
        "difficulty": "hard",
        "topic": "Automation Test",
        "explanation": "Supervised learning trains on labeled examples.",
    },
    {
        "id": "test-8",
        "question": "TEST MODE: What does Git primarily provide?",
        "options": ["Version control", "Database locking", "Memory paging", "CPU scheduling"],
        "correct_index": 0,
        "difficulty": "hard",
        "topic": "Automation Test",
        "explanation": "Git is a distributed version control system.",
    },
    {
        "id": "test-9",
        "question": "TEST MODE: Which traversal commonly uses a queue?",
        "options": ["DFS", "BFS", "Backtracking", "Quick Sort"],
        "correct_index": 1,
        "difficulty": "hard",
        "topic": "Automation Test",
        "explanation": "Breadth First Search commonly uses a queue.",
    },
    {
        "id": "test-10",
        "question": "TEST MODE: Which metric combines precision and recall?",
        "options": ["Accuracy", "F1-score", "Latency", "Throughput"],
        "correct_index": 1,
        "difficulty": "hard",
        "topic": "Automation Test",
        "explanation": "F1-score is the harmonic mean of precision and recall.",
    },
]


def normalize_subject(value, default=None):
    if value is None or value == '':
        return default

    normalized = str(value).strip().lower().replace('-', '_').replace(' ', '_')
    return SUBJECT_ALIASES.get(normalized)


def is_test_mode_enabled(value):
    return str(value).strip().lower() in {'1', 'true', 'yes', 'on'}


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

        test_mode = is_test_mode_enabled(request.query_params.get('test'))
        if test_mode:
            # In test mode, bypass the database and random shuffle completely.
            # Katalon can now rely on stable question text, option order, and answers.
            questions = [
                {**question, "subject": subject}
                for question in TEST_MODE_QUESTIONS
            ]
            return Response({
                "subject": subject,
                "test_mode": True,
                "questions": questions,
                subject: questions,
            })
        
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
