from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("My second Project")

def help(request):
	my_dict = {'insert_help_view': "Help Page!!"}
	return render(request,'AppTwo/help.html', context = my_dict)
