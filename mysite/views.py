# views mysite

from django.shortcuts import render

def index(request):
  context = {
    'judul':'Selamat Datang',
    'subjudul':'Kadosilang',
    'nav': [
      ['/','Home'],
      ['/account','Account'],
      ['/about','About'],
    ]
  }
  return render(request, 'index.html', context)
