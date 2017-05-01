from django.shortcuts import redirect
from django.shortcuts import render

from places.models import Scene


def home_page(request):
  return render(request, 'home.html')


def new_scene(request):
  try:
    lng = request.POST['lng']
    lat = request.POST['lat']
    scene = Scene.objects.create(
      latitude=lat,
      longitude=lng,
      description=request.POST['description'])
    return redirect('/places/%d/' % (scene.id,))
  except KeyError:
    return redirect('/')


def view_scene(request, scene_id):
  scene = Scene.objects.get(id=scene_id)
  return render(request, 'scene.html', {'scene': scene})
