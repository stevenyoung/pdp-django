from django.conf.urls import url
from places import views

urlpatterns = [
  url(r'^api/(?P<scene_id>[-\w]+)',
      views.get_scene_data, name='api_scene_data'),
  url(r'^new$', views.NewSceneView.as_view(), name='new_place'),
  url(r'^home$', views.HomePageView.as_view(), name='places_home'),
  url(r'^near/(?P<lat>[-+]?[0-9]*\.?[0-9]+)/(?P<lng>[-+]?[0-9]*\.?[0-9]+)',
      views.nearby_scenes, name='places_nearby'),
  url(r'^search/(?P<search_term>[-\w]+)',
      views.search_scenes, name='places_search'),
  url(r'^(\d+)$', views.view_scene, name='view_places'),
]
