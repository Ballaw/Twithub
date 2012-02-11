from django.shortcuts import render_to_response, render
from django.template import RequestContext
from areyouatwit.models import TwitOrNot


# Create your views here.

def index(request):
	#return render_to_response('index.html',locals(),context_instance=RequestContext(request))
	return render(request, 'index.html')
