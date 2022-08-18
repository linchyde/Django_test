from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

#setting a basic function gthat takes a http request and returns a response
def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:        
        raise Http404("404 GENERIC ERROR") # remember to adjust the django settings file if needed
    

def num_page_view(request, num_page):

    topics_list = list(articles.keys())
    topic = topics_list[num_page]

    
    return HttpResponseRedirect(reverse('topic-page', args=[topic]))