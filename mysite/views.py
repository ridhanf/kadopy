# views mysite

from django.shortcuts import render

def index(request):
  context = {
    'title':'KADOSILANG',
    'heading':'Selamat Datang',
    'subheading':'di Kadosilang',
  }
  return render(request, 'index.html', context)
