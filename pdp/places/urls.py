from django.conf.urls import url
from places import views

urlpatterns = [
  url(r'^new$', views.NewSceneView.as_view(), name='new_place'),
  url(r'^home$', views.HomePageView.as_view(), name='places_home'),
  url(r'^search/(?P<search_term>[-\w]+)', views.search_scenes, name='places_search'),
  url(r'^(\d+)$', views.view_scene, name='view_places'),
]
