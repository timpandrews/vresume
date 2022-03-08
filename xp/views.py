from django.shortcuts import render
from django.views import generic
from pages.models import Resume

from xp.models import Xp


class XpList(generic.ListView):
    queryset = Xp.objects.filter(status=1).order_by('-created_at')
    template_name = 'xp/xp.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(XpList, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        # Get URL to resume stored in db
        # Hardcoded for name= for now
        resume_url = Resume.objects.filter(name='Tim Andrews').only('filename').first()
        context['resume_url'] = resume_url
        return context

class XpDetail(generic.DetailView):
    model = Xp
    template_name = 'xp/xp_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(XpDetail, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        # Get URL to resume stored in db
        # Hardcoded for name= for now
        resume_url = Resume.objects.filter(name='Tim Andrews').only('filename').first()
        context['resume_url'] = resume_url
        return context
