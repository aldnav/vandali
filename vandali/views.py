from django.shortcuts import render, render_to_response, redirect

def index(request):
	return render(request, 'vandali/index.html', {})