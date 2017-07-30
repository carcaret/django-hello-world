from django.conf.urls import url

from .views import FormHomePageView 
from .views import AboutPageView 
from .views import GreetingPageView 

urlpatterns = [
	url(r'^$', FormHomePageView.as_view()),
        url(r'^greeting$', GreetingPageView.as_view()),
	url(r'^about/?$', AboutPageView.as_view()),
]
