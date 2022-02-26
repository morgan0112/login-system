from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'main/main.html'


class AboutView(TemplateView):
    template_name = 'main/about.html'


class InsulinHelpView(TemplateView):
    template_name = 'main/insulin-help.html'
