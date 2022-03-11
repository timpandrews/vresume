from django.shortcuts import render
from django.views import generic
from pages.models import Resume

from xp.models import Xp, TagType


class XpList(generic.ListView):
    queryset = Xp.objects.filter(status=1).order_by('sort_override', '-created_at')
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

        # Get all Tags for XP
        tags = []
        names = self.object.tags.names()
        for tag in names:
            list = (tag, 'type')
            type = TagType.objects.filter(tag_name=tag).values('tag_type')
            print('type:', type)
            if type:
                type = type.values()[0]['tag_type']
            else:
                type = '99'

            tags.append((tag, type))

        tags = sorted(tags, key=lambda x: (x[1], x[0]))   
        context['tags'] = tags

        # Get related items for XP
        context["related_items"] = self.object.tags.similar_objects()[:4]

        return context
