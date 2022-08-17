from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

#setting a basic function gthat takes a http request and returns a response
def news_view(request, topic):
    return HttpResponse(articles[topic])

def add_view(request, num1, num2):
    #this adds the view from what the user enters
    add_result = num1 + num2
    result = f"{num1}+{num2} = {add_result}"
    return HttpResponse(str(result))
