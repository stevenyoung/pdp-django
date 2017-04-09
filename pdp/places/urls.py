from django.conf.urls import url
from places import views

urlpatterns = [
    url(r'^new$', views.new_scene, name='new_list'),
    url(r'^(\d+)/$', views.view_scene, name='view_list'),
    url(r'^home$', views.home_page, name='home')
]
