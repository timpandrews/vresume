from socketserver import ThreadingUnixStreamServer
from django.shortcuts import render
from django.views import generic
from pages.models import Resume

from xp.models import Xp, TagType


def get_xp_tags(names):
    tags = []
    for tag in names:
        list = (tag, 'type')
        type = TagType.objects.filter(tag_name=tag).values('tag_type')
        if type:
            type = type.values()[0]['tag_type']
        else:
            type = '99'
        tags.append((tag, type))
    tags = sorted(tags, key=lambda x: (x[1], x[0]))
    return tags


def get_tags(tag_type):
    tag_dict = TagType.objects.filter(tag_type=tag_type).order_by(
        'tag_type', 'tag_name').values('tag_name', 'tag_type')
    tags = []
    for tag in tag_dict:
        lst = []
        lst.append(tag['tag_name'])
        lst.append(tag['tag_type'])
        tags.append(lst)
    print(tags)

    return tags


class XpList(generic.ListView):
    def get_queryset(self):
        tag = self.request.GET.get('tag')
        if tag:
            return Xp.objects.filter(tags__name__in=[tag], status=1).order_by('sort_override', '-created_at')
        else:
            return Xp.objects.filter(status=1).order_by('sort_override', '-created_at')
    
    template_name = 'xp/xp.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(XpList, self).get_context_data(**kwargs)
        
        # Get URL to resume stored in db
        # Hardcoded for name= for now
        resume_url = Resume.objects.filter(
            name='Tim Andrews').only('filename').first()
        context['resume_url'] = resume_url

        # Get tags for sidebard
        context['technology_tags'] = get_tags(0)
        context['skill_tags'] = get_tags(1)
        context['job_tags'] = get_tags(2)
        context['personal_tags'] = get_tags(3)

        # Get tag title info
        context['tag_title'] = self.request.GET.get('tag')

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
        resume_url = Resume.objects.filter(
            name='Tim Andrews').only('filename').first()
        context['resume_url'] = resume_url

        # Get Tags for XP
        context['xp_tags'] = get_xp_tags(self.object.tags.names())

        # Get related items for XP
        context["related_items"] = self.object.tags.similar_objects()[:4]

        # Get tags for sidebard
        context['technology_tags'] = get_tags(0)
        context['skill_tags'] = get_tags(1)
        context['job_tags'] = get_tags(2)
        context['personal_tags'] = get_tags(3)
        
        return context
