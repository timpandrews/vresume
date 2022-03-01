from django.db import connection
from django.shortcuts import render
from pages.models import Resume


def index(request):
    # Get URL to resume stored in db
    # Hardcoded for name= for now
    resume_url = Resume.objects.filter(name='Tim Andrews').only('filename').first()

    context = {
        'resume_url': resume_url,
    }
    return render(request, 'pages/index.html', {'context': context})
