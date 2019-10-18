# views mysite

from django.shortcuts import render

def index(request):
  context = {
    'judul':'KADOSILANG',
    'subjudul':'Welcome to Kadosilang',
    'nav': [
      ['/','Home'],
      ['/account','Account'],
      ['/about','About'],
    ]
  }
  return render(request, 'index.html', context)
