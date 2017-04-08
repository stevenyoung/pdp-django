from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
  if request.method == 'POST':
    return HttpResponse(request.POST['post_data'])
  return render(request, 'home.html')
