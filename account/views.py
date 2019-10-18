# views about

from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'judul':'Account',
    'subjudul':'My Account',
    'nav': [
      ['/','Home'],
      ['/account','Account'],
      ['/about','About'],
    ]
  }
  return render(request, 'index.html', context)
