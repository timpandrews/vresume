from django.shortcuts import render

from pages.models import Resume


def home(request):
    # Get URL to resume stored in db
    # Hardcoded for name= for now
    resume_url = Resume.objects.filter(name='Tim Andrews').only('filename').first()

    context = {'resume_url': resume_url,}

    return render(request, 'pages/home.html', {'context': context})


def resume(request):
    # Get URL to resume stored in db
    # Hardcoded for name= for now
    resume_url = Resume.objects.filter(name='Tim Andrews').only('filename').first()

    context = {'resume_url': resume_url,}

    return render(request, 'pages/resume.html', {'context': context})


def contact(request):
    # Get URL to resume stored in db
    # Hardcoded for name= for now
    resume_url = Resume.objects.filter(name='Tim Andrews').only('filename').first()

    context = {'resume_url': resume_url,}

    return render(request, 'pages/contact.html', {'context': context})
