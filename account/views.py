# views about

from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'title':'ACCOUNT',
    'heading':'Selamat Datang',
    'subheading':'di Kadosilang',
  }
  return render(request, 'index.html', context)
