"""
WSGI config for QuizzyPop project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizzypop.settings')
application = get_wsgi_application()
