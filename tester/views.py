# Create your views here.
from django.http import HttpResponse
from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response
from formtest.tester.forms import ClientForm
#def index(request):
#	return direct_to_template(request, template = "index.html")

def showing(request):
	f = request.POST
	f_name = f["firstname"]
	l_name = f["lastname"]
	tdict = {'f_name': f_name, 'l_name': l_name}
	return render_to_response ('show.html', tdict)

def client_list(request):
	if request.method == "POST" or 'None':
		form = ClientForm(request.POST)
		if form.is_valid():
			#cleanform = form.clean()
			form.save()
			form = ClientForm()
		else :
			data = request.POST
			form = ClientForm(data)
		return render_to_response("clients.html", {"form":form})