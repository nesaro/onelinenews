from django.shortcuts import render
from collections import OrderedDict
from .models import *

def headlines(request):
    headlines = HeadLine.objects.all().order_by('-created')
    headlines_dict = OrderedDict()
    for headline in headlines:
        create_date = headline.created.date() 
        if create_date not in headlines_dict:
            headlines_dict[create_date] = []
        headlines_dict[create_date].append(headline)
    return render(request, 'common/headlines.html', {'headlines':headlines_dict})

def headline(request):
    url = request.GET['url']
    headline = HeadLine.objects.get(url=url)
    return render(request, 'common/headline.html', {'headline':headline})

