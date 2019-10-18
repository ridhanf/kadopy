# views about

from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'judul':'Kadosilang',
    'subjudul':'About',
    'nav': [
      ['/','Home'],
      ['/account','Account'],
      ['/about','About'],
    ]
  }
  return render(request, 'index.html', context)
