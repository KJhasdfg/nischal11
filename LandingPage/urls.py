# sentiment_analysis_app/urls.py
from django.urls import path
from .views import analyze_text, result

urlpatterns = [
    path('analyze/', analyze_text, name='analyze_text'),
    path('result/', result, name='result'),
]
