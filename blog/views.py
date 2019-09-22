# views blog

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  context = {
    'judul':'Kadosilang',
    'subjudul':'BLOG',
    'nav': [
      ['/','Home'],
      ['/blog/story','Story'],
      ['/blog/news','News']
    ]
  }
  return render(request, 'blog/index.html', context)
  
def story(request):
  context = {
    'judul':'Kadosilang',
    'subjudul':'Story',
  }
  return render(request, 'blog/index.html', context)

def news(request):
  context = {
    'judul':'Kadosilang',
    'subjudul':'News',
  }
  return render(request, 'blog/index.html', context)

def recent(request):
  return HttpResponse('<h1>Ini adalah recent post </h1>')
