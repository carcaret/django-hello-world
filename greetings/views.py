from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.http import JsonResponse
from .forms import HelloForm
import json

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', {'form': HelloForm()})

class FormHomePageView(FormView):
    template_name = 'index.html'
    form_class = HelloForm
    success_url = '/greeting'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class GreetingPageView(TemplateView):
    def post(self, request, **kwargs):
        form = HelloForm(request.POST)
        name = 'friend'
        if form.is_valid():
            name = form.cleaned_data['your_name']
        return render(request, 'greeting.html', {'name': name})

class AjaxGreetingPageView(TemplateView):
    def post(self, request, **kwargs):
        print(request.body)
        json_data = json.loads(request.body)
        return JsonResponse({'name': json_data.get('new_name', 'missing')})

