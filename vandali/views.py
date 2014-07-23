from django.shortcuts import render, render_to_response, redirect

def index(request):
	return render(request, 'vandali/index.html', {})

def about(request):
	pass

def portfolio(request):
	pass

def contact(request):
	pass

def blog(request):
	pass