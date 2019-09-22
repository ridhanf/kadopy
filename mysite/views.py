# views mysite

from django.shortcuts import render

def index(request):
  context = {
    'judul':'Selamat Datang',
    'subjudul':'Kadosilang',
    'nav': [
      ['/','Home'],
      ['/blog','Blog'],
      ['/about','About'],
      ['/contact','Contact'],
    ]
  }
  return render(request, 'index.html', context)
