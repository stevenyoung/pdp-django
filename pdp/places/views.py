from django.core import serializers
from django.http import JsonResponse
from django.forms.models import model_to_dict

from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views import View

from places.models import Scene
from places.models import Artwork
from places.models import Artist


class HomePageView(View):

  def get(self, request):
    return render(request, 'index.html')


class NewSceneView(View):

  def get(self, request):
    return render(request, 'new_scene_form.html')

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


def view_scene(request, scene_id):
  scene = get_object_or_404(Scene, id=scene_id)
  return render(request, 'scene.html', {'scene': scene})


def search_scenes(request, search_term):
  scenes = Scene.objects.filter(artwork__title__contains=search_term)
  data = serializers.serialize('json', scenes)
  return JsonResponse({'data': data})


def get_scene_data(request, scene_id):
  scene = get_object_or_404(Scene, id=scene_id)
  return JsonResponse({'data': model_to_dict(scene)})
