from django.shortcuts import render, render_to_response, redirect

def index(request):
    return render(request, 'vandali/index.html')

def about(request):
    return render(request, 'vandali/about.html')

def portfolio(request):
    return render(request, 'vandali/portfolio.html')

def contact(request):
    return render(request, 'vandali/contact.html')

def blog(request):
    return render(request, 'vandali/blog.html')