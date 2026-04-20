from django.shortcuts import render

# ---------------------------------------------------------------------------
# Page Views
# ---------------------------------------------------------------------------

def register_view(request):
    return render(request, 'quiz/register.html')

def login_view(request):
    return render(request, 'quiz/login.html')

def logout_view(request):
    # Logout will just be a JS redirect that clears local storage.
    return render(request, 'quiz/login.html')

def index_view(request):
    return render(request, 'quiz/index.html')

def game_view(request):
    return render(request, 'quiz/game.html')

def profile_view(request):
    return render(request, 'quiz/profile.html')
