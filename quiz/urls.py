from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from . import api_views

urlpatterns = [
    # Pages (We will handle login/register via JS to get JWT)
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index_view, name='index'),
    path('game/', views.game_view, name='game'),
    path('profile/', views.profile_view, name='profile'),

    # JWT Auth API
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/register/', api_views.RegisterAPIView.as_view(), name='api_register'),
    
    # Game API
    path('api/v1/questions/', api_views.QuestionBatchAPIView.as_view(), name='api_questions'),
    path('api/v1/submit_score/', api_views.SubmitScoreAPIView.as_view(), name='api_submit_score'),
    path('api/v1/leaderboard/', api_views.LeaderboardAPIView.as_view(), name='api_leaderboard'),
    path('api/v1/analytics/', api_views.AnalyticsAPIView.as_view(), name='api_analytics'),
]
