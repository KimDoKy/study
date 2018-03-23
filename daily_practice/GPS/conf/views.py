from django.views.generic.base import TemplateView
from django.conf import settings

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = {'api':settings.MAP_API}
        return context
