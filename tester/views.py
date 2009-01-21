# Create your views here.
from django.http import HttpResponse
from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response

#def index(request):
#	return direct_to_template(request, template = "index.html")

def showing(request):
	f = request.POST
	f_name = f["firstname"]
	l_name = f["lastname"]
	tdict = {'f_name': f_name, 'l_name': l_name}
	return render_to_response ('show.html', tdict)
