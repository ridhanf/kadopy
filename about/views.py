# views about

from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'judul':'Kadosilang',
    'subjudul':'ABOUT',
    'nav': [
      ['/','Home'],
      ['/blog','Blog'],
      ['/about','About'],
      ['/contact','Contact'],
    ]
  }
  return render(request, 'about.html', context)