# TemplateView use with CBV
from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = 'index.html'


class TestPage(TemplateView):
    template_name = "test.html"


class TanksPage(TemplateView):
    template_name = "thanks.html"

