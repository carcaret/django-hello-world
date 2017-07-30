from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from .forms import HelloForm

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', {'form': HelloForm()})

class AboutPageView(TemplateView):
    template_name = 'about.html'

class GreetingPageView(TemplateView):
    def post(self, request, **kwargs):
        form = HelloForm(request.POST)
        name = 'friend'
        if form.is_valid():
            name = form.cleaned_data['your_name']
        return render(request, 'greeting.html', {'name': name})

class FormHomePageView(FormView):
    template_name = 'index.html'
    form_class = HelloForm
    success_url = '/greeting'

