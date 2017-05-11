from django.shortcuts import redirect
from django.shortcuts import render

from django.views import View

from places.models import Scene
from places.models import Artwork
from places.models import Artist


class HomePageView(View):

  def get(self, request):
    return render(request, 'index.html')

  def post(self, request):
    try:
      title = request.POST['artwork']
      posted_artist = request.POST['artist']
      artist_ = Artist.objects.create(full_name=posted_artist)
      artwork_ = Artwork.objects.create(title=title, artist=artist_)
      lng = request.POST['lng']
      lat = request.POST['lat']
      scene = Scene.objects.create(
        artwork=artwork_,
        latitude=lat,
        longitude=lng,
        description=request.POST['description'])
      return redirect('/places/%d/' % (scene.id))
    except KeyError:
      return redirect('/')


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


def search(request, search_term):
  print(search_term)
  pass
